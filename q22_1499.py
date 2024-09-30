

class Solution:
    from collections import deque
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()
        ans = float('-inf')

        for x,y in points:
            while q and x - q[0][1] >k :
                q.popleft()
            if q:
                ans = max(ans,q[0][0]+y+x)
            while q and q[-1][0] <= y-x:
                q.pop()
            q.append((y-x,x))
        return ans

