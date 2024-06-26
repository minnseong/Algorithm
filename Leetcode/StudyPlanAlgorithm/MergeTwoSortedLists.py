# LeetCode 2021 . 12 . 22
# Study Plan - Algorithm Day 10 21. Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        head = ListNode()
        cur = head
        
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
                
            cur = cur.next
        
        if list1 is None:
            cur.next = list2
        else:
            cur.next = list1
        
        return head.next