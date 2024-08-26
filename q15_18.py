class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quad  = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                left,right = j+1,n-1
                while left<right:
                    curr = nums[i] + nums[j] + nums[right] + nums[left]
                    if curr == target:
                        quad.add((nums[i],nums[j],nums[right],nums[left]))
                        left += 1
                        right -= 1

                    if curr >target:
                        right -= 1
                    elif curr <target:
                        left += 1
        return [list(qua) for qua in quad]
                    
