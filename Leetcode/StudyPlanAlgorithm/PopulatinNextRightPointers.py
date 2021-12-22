# LeetCode 2021 . 12 . 22
# Study Plan - Algorithm Day 8 116. Populating Next Right Pointers in Each Node

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        r = root
        while r and r.left:
            cur = r
            while cur:
                cur.left.next = cur.right
                cur.right.next = cur.next and cur.next.left
                cur = cur.next
            r = r.left
        
        return root