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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode tmp1=l1;
        ListNode tmp2=l2;
        ListNode tmp3=null;
        ListNode head3=null;
        int previous=0;
        while(tmp1!=null && tmp2!=null)
        {
            int curr=tmp1.val+tmp2.val+previous;
            if(curr>9)
            {
                ListNode newNode=new ListNode(curr%10);
                previous=curr/10;
                if(tmp3==null)
                {
                    tmp3=newNode;
                    head3=newNode;
                }
                else
                {
                    tmp3.next=newNode;
                    tmp3=newNode;
                }
            }
            else
            {
                ListNode newNode=new ListNode(curr);
                 previous=0;
                if(tmp3==null)
                {
                    tmp3=newNode;
                    head3=newNode;
                }
                else
                {
                    tmp3.next=newNode;
                    tmp3=newNode;
                }
            }
            tmp1=tmp1.next;
            tmp2=tmp2.next;
        }
        while(tmp1!=null)
        {
            int curr=tmp1.val+previous;
            if(curr>9)
            {
                ListNode newNode=new ListNode(curr%10);
                previous=curr/10;
                if(tmp3==null)
                {
                    tmp3=newNode;
                    head3=newNode;
                }
                else
                {
                    tmp3.next=newNode;
                    tmp3=newNode;
                }
            }
            else
            {
                ListNode newNode=new ListNode(curr);
                previous=0;
                if(tmp3==null)
                {
                    tmp3=newNode;
                    head3=newNode;
                }
                else
                {
                    tmp3.next=newNode;
                    tmp3=newNode;
                }
            }
            tmp1=tmp1.next;
        }
        while(tmp2!=null)
        {
            int curr=tmp2.val+previous;
            if(curr>9)
            {
                ListNode newNode=new ListNode(curr%10);
                previous=curr/10;
                if(tmp3==null)
                {
                    tmp3=newNode;
                    head3=newNode;
                }
                else
                {
                    tmp3.next=newNode;
                    tmp3=newNode;
                }
            }
            else
            {
                ListNode newNode=new ListNode(curr);
                previous=0;
                if(tmp3==null)
                {
                    tmp3=newNode;
                    head3=newNode;
                }
                else
                {
                    tmp3.next=newNode;
                    tmp3=newNode;
                }
            }
            tmp2=tmp2.next;
        }
        if(previous!=0)
        {
            ListNode newNode=new ListNode(previous);
            tmp3.next=newNode;
            tmp3=newNode;
        }
        return head3;
    }
}