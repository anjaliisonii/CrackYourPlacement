# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        count=0
        while (n):
            fast=fast.next
            n-=1
            if fast==None:
                return head.next
        pre=head
        second=head
        while fast!=None:
            pre=second
            second=second.next
            fast=fast.next
        pre.next=second.next
        return head
        