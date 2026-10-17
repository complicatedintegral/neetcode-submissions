class Solution:
    def ListNode(self, val):
        self.val = None
        self.next = None
        
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = 0

        while True: # identifying the loop, since it is guaranteed according to the question
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0

        while slow != slow2: # finding the entry point of the loop to identify the repeated integer
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow2