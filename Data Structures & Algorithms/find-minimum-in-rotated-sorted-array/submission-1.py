class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        i = 0
        j = len(nums) - 1

        while i <= j:

            if nums[i] <= nums[j]:
                return nums[i]
            
            m = (i+j) // 2

            if nums[m] > nums[j]:
                i = m + 1

            else:
                j = m
            
        return i