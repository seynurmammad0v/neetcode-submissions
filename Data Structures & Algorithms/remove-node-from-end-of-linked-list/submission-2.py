# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        prev = None
        first = head
        size = 0
        while first:
            first = first.next
            size+=1

        if size == 1:
            return None

        second = head
        prev = head
        

        for i in range(size):
            if i == size-n:
                if i == 0:
                    head = head.next
                    return head
                prev.next = second.next
                return head
            prev = second
            second = second.next

        return head