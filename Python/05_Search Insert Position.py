# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target):
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if target>nums[mid]:
                start=mid+1
            else:
                end=mid-1
        return start