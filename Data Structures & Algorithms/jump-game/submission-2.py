class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        currJump = 0
        maxJump = 0

        for i in range(n):
            maxJump = max(maxJump, i + nums[i])
            if maxJump >= n-1:
                return True

            if i == currJump:
                if i == maxJump:
                    return False
                else:
                    currJump = maxJump

        return False

