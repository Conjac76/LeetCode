# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        strNum = ""
        strNum2 = ""

        while l2 != None:
            strNum2 += str(l2.val)
            l2 = l2.next

        while l1 != None:
            strNum += str(l1.val)
            l1 = l1.next
        print(strNum)
        print(strNum2)
        
        if len(strNum) == 0 or len(strNum2) == 0:
            return None

        reverseNum = ""
        reverseNum2 = ""
        for i in range(len(strNum) -1, -1, -1):
            reverseNum += strNum[i]
        for i in range(len(strNum2) -1, -1, -1):
            reverseNum2 += strNum2[i]

        reverseNum = int(reverseNum)
        reverseNum2 = int(reverseNum2)

        totalReverseNum = reverseNum + reverseNum2
        totalReverseNum = str(totalReverseNum)

        result = ListNode()
        curr = result

        for i in range(len(totalReverseNum) -1, -1, -1):
            curr.next = ListNode(int(totalReverseNum[i]))
            curr = curr.next


        return result.next