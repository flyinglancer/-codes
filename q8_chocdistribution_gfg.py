class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        
        A.sort()
        
        mind = float('inf')
        
        for i in range(N-M+1):
            strt = A[i]
            end = A[i+M-1]
            
            mind = min(mind,end-strt)
            
        return mind
