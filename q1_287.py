#q1 287
class Solution(object):
    def findDuplicate(self, nums):
        tt = nums[0]
        hr = nums[0]

        while True:
            tt = nums[tt]
            hr = nums[nums[hr]]
            if tt == hr:
                break
        
        tt = nums[0]
        while tt != hr:
            tt = nums[tt]
            hr = nums[hr]

        return tt
