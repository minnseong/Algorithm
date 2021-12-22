# LeetCode 2021 . 12 . 23
# Study Plan - Algorithm Day 10 206. Reverse Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        p = head
        q = None
        r = None
        
        while p != None:
            q = p
            p = p.next
            q.next = r
            r = q
        
        return q
            