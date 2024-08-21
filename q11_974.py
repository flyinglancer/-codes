class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        remain = {0: 1}
        prefik = 0
        count  = 0

        for num in nums:
            prefik += num

            remainc = prefik % k

            if remainc <0:
                remainc = remainc + k
            if remainc in remain:
                count += remain.get(remainc)
            remain[remainc] = remain.get(remainc,0) + 1
        return count 
        
