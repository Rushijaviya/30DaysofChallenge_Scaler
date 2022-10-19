# Reversing the equation
# https://practice.geeksforgeeks.org/problems/reversing-the-equation2205/1

#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        ans=""
        idx=len(s)-1
        while idx>=0:
            if s[idx] in '+-*/':
                ans+=s[idx]
                idx-=1
            else:
                j=idx-1
                while j>=0 and s[j] not in '+-*/':
                    j-=1
                ans+=s[j+1:idx+1]
                idx=j
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends