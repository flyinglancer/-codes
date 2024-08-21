class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupli = []
        for i in range(len(nums)):
            index = abs(nums[i]) -1

            if nums[index] < 0:
                dupli.append(index+1)
            else:
                nums[index] = -nums[index]
        return dupli
