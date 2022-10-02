# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        n,m=len(nums1),len(nums2)
        start=0
        end=n
        while start<=end:
            cut1=(start+end)//2
            cut2=(n+m+1)//2-cut1
            l1=nums1[cut1-1] if cut1>0 else float('-inf')
            l2=nums2[cut2-1] if cut2>0 else float('-inf')
            r1=nums1[cut1] if cut1<n else float('inf')
            r2=nums2[cut2] if cut2<m else float('inf')
            if l1<=r2 and l2<=r1:
                if (n+m)%2:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                end=cut1-1
            else:
                start=cut1+1
        return 0