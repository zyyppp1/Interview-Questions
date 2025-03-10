
 

def removeDuplicates(nums):
    dict={}
    p=0
    for i in range(len(nums)):
        if nums[i] not in dict:
            nums[p]=nums[i]
            dict[nums[i]]=1
            p+=1
    return p
