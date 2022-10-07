# Killing Spree
# https://practice.geeksforgeeks.org/problems/killing-spree3020/1

#User function Template for python3

class Solution:
    def killinSpree (self, n):
        # code here
        
        def vaild(target,n):
            temp=(target*(target+1)*(2*target+1))//6
            return n>=temp
        
        start=1
        end=n
        ans=-1
        while start<=end:
            mid=(start+end)//2
            if vaild(mid,n):
                ans=mid
                start=mid+1
            else:
                end=mid-1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.killinSpree(N);
        print(ans)




# } Driver Code Ends