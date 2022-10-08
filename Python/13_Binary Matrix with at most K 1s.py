# Binary Matrix with at most K 1s
# https://practice.geeksforgeeks.org/problems/largest-square-in-a-binary-matrix-with-at-most-k-1s-for-multiple-queries/1

#User function Template for python3

class Solution:
    def largestSquare(self, M, R, C, K, Q, q_i, q_j):
        countDP = [[0 for x in range(C)]
                  for x in range(R)] 
     
        countDP[0][0] = M[0][0] 
         
        for i in range(1, R):
            countDP[i][0] = (countDP[i - 1][0] +
                                  M[i][0])
        for j in range(1, C):
            countDP[0][j] = (countDP[0][j - 1] +
                              M[0][j])
        for i in range(1, R):
            for j in range(1, C):
                countDP[i][j] = (M[i][j] +
                                countDP[i - 1][j] +
                                countDP[i][j - 1] -
                                countDP[i - 1][j - 1])
        
        res = []
        
        for q in range(0,Q):
            i = q_i[q]
            j = q_j[q]
             
            min_dist = min(i, j, R - i - 1, 
                                 C - j - 1)
            ans = -1
            l = 0
            u = min_dist
             
            while (l <= u):
                mid = int((l + u) / 2) 
                x1 = i - mid
                x2 = i + mid 
                y1 = j - mid
                y2 = j + mid 
                count = countDP[x2][y2]
                 
                if (x1 > 0):
                        count -= countDP[x1 - 1][y2] 
                if (y1 > 0):
                        count -= countDP[x2][y1 - 1]
                if (x1 > 0 and y1 > 0): 
                        count += countDP[x1 - 1][y1 - 1]
                if (count <= K): 
                        ans = 2 * mid + 1
                        l = mid + 1
                else:
                    u = mid - 1
            
            if ans==-1:
                ans = 0
            res.append(ans)
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        R,C=map(int,input().split())
        M=[]
        
        for i in range(R):
            temp=list(map(int,input().split()))
            M.append(temp)
            
        K,Q=list(map(int,input().split()))
        
        q_i=list(map(int,input().split()))
        q_j=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.largestSquare(M,R,C,K,Q,q_i,q_j)
        
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends