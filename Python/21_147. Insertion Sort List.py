# 147. Insertion Sort List
# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head):
        ans=ListNode(0)
        curr=head
        while curr:
            prev=ans
            while prev.next and prev.next.val<curr.val:
                prev=prev.next
            temp=curr.next
            curr.next=prev.next
            prev.next=curr
            curr=temp
        return ans.next