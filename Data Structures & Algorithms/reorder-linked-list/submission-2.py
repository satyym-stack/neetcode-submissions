# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        # Reach the first node of the second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Split
        second = slow.next
        slow.next = None
        # Reverse the other half of the linked list
        previous = None
        current = second
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        # Merging both the halves alternatively
        first = head
        second = previous
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

         

