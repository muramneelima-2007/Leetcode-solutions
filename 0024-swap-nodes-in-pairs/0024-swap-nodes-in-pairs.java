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
    public ListNode swapPairs(ListNode head) {
        ListNode tmp=head;
        int count=0;
        List<Integer> odd=new ArrayList<>();
        List<Integer> even=new ArrayList<>();
        while(tmp!=null)
        {
            count++;
            if(count%2!=0)
            {
               odd.add(tmp.val);
            }
            else
            {
                even.add(tmp.val);
            }
            tmp=tmp.next;
        }
        int eve=even.size();
        int od=odd.size();
        ListNode head1=null;
        ListNode tmp1=null;
        int ind1=0;
        int ind2=0;
        while(eve!=ind1 && od!=ind2)
        {
          ListNode newNode1=new ListNode(even.get(ind1++));
          ListNode newNode2=new ListNode(odd.get(ind2++));
          if(tmp1==null)
          {
            head1=newNode1;
            newNode1.next=newNode2;
            tmp1=newNode2;
          }
          else
          {
            tmp1.next=newNode1;
            newNode1.next=newNode2;
            tmp1=newNode2;
          }
        }
        if(count%2!=0 && count!=1)
        {
            ListNode newNode=new ListNode(odd.get(count/2));
            tmp1.next=newNode;
            tmp1=newNode;
        }
        else if(count%2!=0 && count==1)
        {
            ListNode newNode=new ListNode(odd.get(count/2));
            head1=newNode;
        }
        return head1;
    }
}