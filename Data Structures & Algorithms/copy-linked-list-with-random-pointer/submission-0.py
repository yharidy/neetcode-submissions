"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        index = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            index[curr] = copy
            curr=curr.next
        curr = head
        while curr:
            index[curr].next = None if curr.next is None else index[curr.next]
            index[curr].random = None if curr.random is None else index[curr.random]
            curr = curr.next
        return index[head]