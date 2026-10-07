# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None
        l1_val = 0 if l1 is None else l1.val
        l2_val = 0 if l2 is None else l2.val
        sums = l1_val + l2_val
        new_node = ListNode(val=sums%10)
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
        if rem:=sums//10:
            if l1:
                l1.val+=rem
            elif l2:
                l2.val+=rem
            else:
                l1 = ListNode(val=sums//10)
        new_node.next = self.addTwoNumbers(l1,l2)
        return new_node