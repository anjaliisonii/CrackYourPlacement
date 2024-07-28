# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p=0
        q=0
        carry=0
        dummy=ListNode(-1)
        curr=dummy
        while l1!=None or l2!=None or carry==1:
            p=l1.val if l1!=None else 0
            q=l2.val if l2!=None else 0
            sum1=p+q+carry
            carry=sum1//10
            curr.next=ListNode(sum1%10)
            curr=curr.next
            l1=l1.next if l1!=None else None
            l2=l2.next if l2!=None else None
        return dummy.next

       