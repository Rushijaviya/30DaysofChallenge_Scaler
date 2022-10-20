# 456. 132 Pattern
# https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums):
        stack=[]
        middle=float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<middle:
                return True
            while stack and nums[i]>stack[-1]:
                middle=stack.pop()
            stack.append(nums[i])
        return False