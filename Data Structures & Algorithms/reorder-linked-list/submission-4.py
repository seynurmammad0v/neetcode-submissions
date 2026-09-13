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


        second = slow.next
        slow.next = None
        prev = None

        while second != None:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node


        reversed_list = prev

        while reversed_list:
            head_next_node, reversed_next_node = head.next, reversed_list.next
            head.next = reversed_list
            reversed_list.next = head_next_node
            reversed_list = reversed_next_node
            head = head_next_node

       
        
