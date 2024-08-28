class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n =  len(cardPoints)
        mac = sum(cardPoints[:k])
        curr = mac
        for i in range(k):
            curr += cardPoints[n-1-i] - cardPoints[k-1-i]
            mac = max(curr,mac)
        return mac

        



