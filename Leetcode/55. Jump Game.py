class Solution(object):
    def canJump(self, nums):
        path = 0 
        i=0
        while i <=path :
            path=max(path,nums[i]+i)
            i+=1
            if path >= len(nums)-1:
                return True
        return False