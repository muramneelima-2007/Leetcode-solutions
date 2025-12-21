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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode tmp=head;
        int Previousval=-100;
        ListNode previous=null;
        while(tmp!=null)
        {
            if(Previousval==tmp.val)
            {
                if(tmp.next!=null)
                {
                    previous.next=tmp.next;
                    tmp=tmp.next;
                }
                else
                {
                   previous.next=null;
                   tmp=tmp.next;
                }
            }
            else
            {
                Previousval=tmp.val;
                previous=tmp;
                tmp=tmp.next;
            }
        }
       return head;
    }
}