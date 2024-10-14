class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def beacktrack(s='',left=0,right=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                beacktrack(s + "(",left+1,right)
            if right < left:
                beacktrack(s + ")" ,left,right+1)
        beacktrack()
        return result
