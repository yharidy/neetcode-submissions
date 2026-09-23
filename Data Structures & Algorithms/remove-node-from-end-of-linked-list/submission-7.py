# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l+=1
            curr = curr.next
        to_remove = l - n
        if to_remove == 0:
            return head.next
        prev = head
        for i in range(to_remove-1):
            prev = prev.next

        prev.next = prev.next.next
        return head

