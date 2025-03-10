def majorityElement(nums):
    nums.sort()
    majority= nums[len(nums) // 2]
    return majority
