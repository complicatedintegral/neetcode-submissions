# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head):
        curr = head 
        prev = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return 

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None # splitting the second list apart from the first list

        first = head
        second = self.reverseList(second) # reversing the second question as required in the question

        while second:

            fn = first.next
            sn = second.next

            first.next = second
            second.next = fn

            first = fn
            second = sn

        

        