class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxr = 0
        for i in range(len(nums)):
            if i > maxr:
                return False
            if maxr>= len(nums)-1:
                return True
            maxr  = max(maxr,i+nums[i])
