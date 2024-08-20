class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        noi = {}

        for i,num in enumerate(nums):
            compi = target - num

            if compi in noi:
                return [noi[compi],i]
            noi[num] = i




        
