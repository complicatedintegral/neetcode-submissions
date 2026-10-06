class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = 0
        best = nums[0]

        for i in nums:
            if curr < 0:
                curr = 0
            curr += i
            best = max(curr, best)

        return best