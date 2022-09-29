# 51. N-Queens
# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n):
        
        def vaild(nums,n):
            for i in range(n):
                if nums[i]==nums[n] or (abs(nums[i]-nums[n])==n-i):
                    return 0
            return 1
    
        def rec(idx,nums,temp):
            if idx==n:
                ans.append(temp)
                return 
            for j in range(n):
                nums[idx]=j
                if vaild(nums,idx):
                    t='.'*n
                    rec(idx+1,nums,temp+[t[:j]+'Q'+t[j+1:]])

        ans=[]
        rec(0,[-1]*n,[])
        return ans