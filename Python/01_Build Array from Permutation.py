# 1920. Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums):
        '''
        # Approach 1
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
        '''

        # Approach 2        
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]+n*(nums[nums[i]]%n)
        for i in range(n):
            nums[i]//=n
        return nums