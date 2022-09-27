# 1502. Can Make Arithmetic Progression From Sequence
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        x=arr[1]-arr[0]
        for i in range(2,len(arr)):
            if arr[i]-arr[i-1]!=x:
                return False
        return True