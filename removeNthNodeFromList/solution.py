# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        tempNode = head
        while count < n and head != None:
            head = head.next
            count += 1

        if head is None:
            return curr.next

        while head.next is not None:
            head = head.next
            tempNode = tempNode.next

        tempNode.next = tempNode.next.next

        return curr