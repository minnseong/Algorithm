// LeetCode 2021 . 12 . 16
// Study Plan - Algorithm Day 5 876. Middle of the Linked List
package Leetcode.StudyPlanAlgorithm;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        
        ListNode firstPoint = head;
        ListNode secondPoint = head;
        
        while(secondPoint != null && secondPoint.next != null) {
            secondPoint = secondPoint.next.next;
            firstPoint = firstPoint.next;
        }
        
        return firstPoint;
    }
}