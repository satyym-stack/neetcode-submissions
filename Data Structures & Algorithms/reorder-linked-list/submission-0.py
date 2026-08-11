# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
         nodes = []
         current = head 
         while current:
            nodes.append(current)
            current = current.next

         left = 0
         right = len(nodes) - 1
         while left < right:
            nodes[left].next = nodes[right]
            nodes[right].next = nodes[left + 1]
            left = left + 1
            right = right - 1
         nodes[left].next = None