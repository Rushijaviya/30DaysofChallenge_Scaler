# 2033. Minimum Operations to Make a Uni-Value Grid
# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution:
    def minOperations(self, grid, x):
        l=[]
        for i in grid:
            l+=i
        l.sort()
        temp=l[len(l)//2]
        count=0
        for i in range(len(l)):
            diff=abs(l[i]-temp)
            if diff%x:
                return -1
            count+=(diff//x)
        return count