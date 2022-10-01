# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums, target):
        '''
        # Approach 1
        return [bisect_left(nums,target),bisect_right(nums,target)-1] if target in nums else [-1,-1]
        '''

        # Approach 2
        def search(l,tar):
            start=0
            end=len(l)-1
            while start<=end:
                mid=(start+end)//2
                if tar<=l[mid]:
                    end=mid-1
                else:
                    start=mid+1
            return start
        
        return [search(nums,target),search(nums,target+1)-1] if target in nums else [-1,-1]