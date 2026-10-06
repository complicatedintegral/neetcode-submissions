class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        n = len(nums)
        c = 0
        m = 0
        j = 0

        for i in range(n):
            m = max(m, nums[i] + i)
            if m >= n-1:
                return j+1

            if i == c:
                if i == m:
                    return -1
                else:
                    j += 1
                    c = m

        return -1