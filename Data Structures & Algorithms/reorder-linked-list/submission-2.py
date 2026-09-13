# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow != None:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        reversed_list = prev
        first = head
        while reversed_list.next != None:
            next_node = first.next
            first.next = reversed_list
            reversed_list = reversed_list.next
            first.next.next = next_node
            first = next_node

       
        
