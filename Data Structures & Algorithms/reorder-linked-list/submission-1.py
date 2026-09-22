# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Brute force
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = [head]
        while head.next:
            l.append(head.next)
            head = head.next
        i, j = 0, len(l)-1
        while i <j:
            l[i].next = l[j]
            i += 1
            if i>=j:
                break
            l[j].next = l[i]
            j-=1
        l[i].next = None

# recursion


        