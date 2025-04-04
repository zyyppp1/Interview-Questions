import requests
from datetime import datetime, timedelta, timezone
from collections import defaultdict
from typing import List, Dict, Set, Tuple, Any

# API配置常量
USER_KEY = "c01b75d56ae6ce15f2309cc7b9f1"
TEST_DATA_URL = f"https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset?userKey={USER_KEY}"
TEST_RESULT_URL = f"https://candidate.hubteam.com/candidateTest/v3/problem/test-result?userKey={USER_KEY}"
REAL_DATA_URL = f"https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey={USER_KEY}"
REAL_RESULT_URL = f"https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey={USER_KEY}"

def timestamp_to_utc_date(ts: int) -> str:
    """将毫秒级时间戳转换为UTC日期字符串 (YYYY-MM-DD)"""
    return datetime.fromtimestamp(ts / 1000, tz=timezone.utc).strftime('%Y-%m-%d')

def fetch_data(test_mode: bool = True) -> List[Dict[str, Any]]:
    """从API获取通话数据
    
    Args:
        test_mode: 如果为True，获取测试数据；否则获取实际数据
    
    Returns:
        通话记录列表
    """
    url = TEST_DATA_URL if test_mode else REAL_DATA_URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"API Response: {response.status_code}")
        return response.json().get('callRecords', []) if test_mode else response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        raise

def post_result(results: List[Dict[str, Any]], test_mode: bool = True) -> requests.Response:
    """向API发送计算结果
    
    Args:
        results: 计算结果列表
        test_mode: 如果为True，发送到测试端点；否则发送到实际端点
    
    Returns:
        API响应对象
    """
    url = TEST_RESULT_URL if test_mode else REAL_RESULT_URL
    try:
        response = requests.post(url, json={"results": results})
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error posting results: {e}")
        raise

def split_calls_by_day(calls: List[Dict[str, Any]]) -> Dict[Tuple[int, str], List[Dict[str, Any]]]:
    """将通话记录按客户ID和日期分组
    
    如果一个通话跨多天，会将其拆分为每天的部分
    
    Args:
        calls: 通话记录列表
    
    Returns:
        按(客户ID, 日期)分组的通话部分字典
    """
    result = defaultdict(list)
    for call in calls:
        cid = call['customerId']
        call_id = call['callId']
        start = call['startTimestamp']
        end = call['endTimestamp']

        # 将时间戳转换为UTC日期时间，并重置为当天开始时间点
        start_dt = datetime.fromtimestamp(start / 1000, tz=timezone.utc).replace(
            hour=0, minute=0, second=0, microsecond=0)
        end_dt = datetime.fromtimestamp(end / 1000, tz=timezone.utc).replace(
            hour=0, minute=0, second=0, microsecond=0)
        
        # 计算通话跨越的天数
        num_days = (end_dt - start_dt).days + 1

        # 将通话拆分为每天的部分
        for i in range(num_days):
            day_start = int((start_dt + timedelta(days=i)).timestamp() * 1000)
            day_end = int((start_dt + timedelta(days=i + 1)).timestamp() * 1000)
            
            # 获取当天通话部分的起止时间
            part_start = max(start, day_start)
            part_end = min(end, day_end)
            
            # 只有当通话在当天确实有部分时才添加
            if part_start < part_end:
                date = timestamp_to_utc_date(part_start)
                result[(cid, date)].append({
                    "callId": call_id,
                    "start": part_start,
                    "end": part_end
                })
    return result

def calculate_max_concurrency(calls_by_customer_date: Dict[Tuple[int, str], List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    """计算每个客户每天的最大并发通话数
    
    Args:
        calls_by_customer_date: 按客户和日期分组的通话记录
    
    Returns:
        结果列表，每项包含客户ID、日期、最大并发数、达到最大并发的时间戳和通话ID列表
    """
    results = []
    for (cid, date), call_list in calls_by_customer_date.items():
        # 创建事件列表
        events = []
        for call in call_list:
            # 1表示开始事件，-1表示结束事件
            events.append((call['start'], 1, call['callId'])) 
            events.append((call['end'], -1, call['callId']))

        # 排序：先按时间戳，对于相同时间戳，结束事件(-1)优先于开始事件(1)
        events.sort(key=lambda x: (x[0], x[1]))
        
        # 追踪当前活跃通话
        current = set()
        max_count = 0
        max_timestamp = 0
        max_call_ids = []

        # 扫描所有事件
        for ts, evt_type, call_id in events:
            if evt_type == -1:  # 结束事件
                current.discard(call_id)
            else:  # 开始事件
                current.add(call_id)
                # 检查是否有新的最大并发
                if len(current) > max_count:
                    max_count = len(current)
                    max_timestamp = ts
                    max_call_ids = list(current)

        # 添加结果
        results.append({
            "customerId": cid,
            "date": date,
            "maxConcurrentCalls": max_count,
            "timestamp": max_timestamp,
            "callIds": max_call_ids
        })
    return results

def process_calls(calls: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """处理通话记录的主函数
    
    Args:
        calls: 通话记录列表
    
    Returns:
        处理结果列表
    """
    calls_by_day = split_calls_by_day(calls)
    return calculate_max_concurrency(calls_by_day)

def main(test_mode: bool = True):
    """主函数
    
    Args:
        test_mode: 如果为True，使用测试API；否则使用实际API
    """
    # 获取通话数据
    calls = fetch_data(test_mode)
    print(f"Retrieved {len(calls)} call records")
    
    # 计算最大并发通话数
    result_data = process_calls(calls)
    print(f"Generated {len(result_data)} result entries")
    
    # 发送结果
    response = post_result(result_data, test_mode)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    return response.status_code == 200

if __name__ == "__main__":
    # 先使用测试数据验证
    print("Testing with example data...")
    if main(test_mode=True):
        print("Test successful! Proceeding with real data.")
        # 如果测试成功，再处理实际数据
        success = main(test_mode=False)
        print(f"Final submission {'successful' if success else 'failed'}")
    else:
        print("Test failed. Please check your implementation.")