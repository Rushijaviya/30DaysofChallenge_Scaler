# 1828. Queries on Number of Points Inside a Circle
# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution:
    def countPoints(self, points, queries):
        ans=[]
        for x1,y1,r in queries:
            count=0
            for x2,y2 in points:
                dis=(x1-x2)**2+(y1-y2)**2
                if dis<=r**2:
                    count+=1
            ans.append(count)
        return ans