# 2181. Merge Nodes in Between Zeros
# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head):
        ans=ListNode(0)
        res=ans
        curr=head.next
        while curr:
            s=0
            while curr and curr.val!=0:
                s+=curr.val
                curr=curr.next
            res.next=ListNode(s)
            res=res.next
            if curr:
                curr=curr.next
        return ans.next