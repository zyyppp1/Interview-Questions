def rotate (nums, k):
        r = k % len(nums)
        if r > 0:
            nums[:r], nums[r:] = nums[-r:], nums[:-r]
            
