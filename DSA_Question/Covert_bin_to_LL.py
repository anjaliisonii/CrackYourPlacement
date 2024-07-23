# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin=""
        temp=head
        if head is None:
            return
        while temp is not None:
            bin+=str(temp.val)
            temp=temp.next
        return int(bin,2)
        