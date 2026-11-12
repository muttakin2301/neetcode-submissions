# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head

        while current.next and current.next.next:
            tail = current

            while tail.next.next:
                tail = tail.next

            nxt = current.next

            current.next = tail.next
            tail.next.next = nxt
            tail.next = None
            current = nxt