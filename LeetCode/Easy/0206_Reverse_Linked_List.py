"""
Problem: Reverse Linked List
Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Linked List
- Iteration
- Two Pointers

Idea:
Traverse the linked list while reversing the direction
of each node's next pointer.
Keep track of the previous and current nodes until
the entire list is reversed.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev