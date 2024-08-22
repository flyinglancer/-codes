class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        maxwater = 0
        while left<right:
            width = right-left
            curr = min(height[left],height[right])
            maxwater = max(maxwater,curr*width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            
        return maxwater

