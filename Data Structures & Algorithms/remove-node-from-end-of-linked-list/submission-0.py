# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        l = 0
        testNode = head
        while testNode:
            l += 1
            testNode = testNode.next

        dummy = ListNode()
        mainNode = dummy 
        x = l - n

        for i in range(x):
            mainNode.next = head
            head = head.next
            mainNode = mainNode.next

        head = head.next
        mainNode.next = head

        return dummy.next