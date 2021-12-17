// LeetCode 2021 . 12 . 17
// Study Plan - Algorithm Day 5 19. Remove Nth Node From End of List
package Leetcode.StudyPlanAlgorithm;

public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        int cnt = 0;
        ListNode p = new ListNode();
        ListNode q = new ListNode();
        p.next = head;
        q.next = head;
        
        while(p != null) {
            p = p.next;
            cnt++;
        }
        
        cnt = cnt - n -1;
        
        for (int i = 0 ; i < cnt; i++) {
            q = q.next;
        }
        
        q.next = q.next.next;
        
        if (cnt <= 0) {
            return q.next;
        }
        return head;
    }
}