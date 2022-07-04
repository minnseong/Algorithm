# LeetCode 07/04 2022
# Study Plan Algorithm2 - Day 3 Two Pointers
# 82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> ListNode:
        ln = ListNode(0, head)

        cur = ln
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                cur.next = head.next
            else:
                cur = cur.next
            head = head.next

        return ln.next