# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNodes = []
        
        def cycle(head):
            if head is None:
                return False 

            if head in visitedNodes:
                return True

            visitedNodes.append(head)
            return cycle(head.next)

        return cycle(head)
