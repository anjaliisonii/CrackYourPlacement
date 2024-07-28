# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        mid=self.middleNode(head)
        left=self.sortList(head)
        right=self.sortList(mid)
        return self.merge(left,right)
    def middleNode(self,head):
        slow=head
        fast=head.next
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        return mid
    def merge(self,left,right):
        dummy=ListNode(-1)
        curr=dummy
        while left!=None and right!=None:
            if left.val<=right.val:
                curr.next=left
                left=left.next
            else:
                curr.next=right
                right=right.next
            curr=curr.next
        if left==None:
            curr.next=right
        else:
            curr.next=left
        return dummy.next