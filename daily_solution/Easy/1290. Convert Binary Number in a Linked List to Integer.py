# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        #linked list converted into array
        num = 0
        while head:
            num = num * 10 + head.val 
            head = head.next

        #integer can converted into integer value
        return int(str(num),2)
