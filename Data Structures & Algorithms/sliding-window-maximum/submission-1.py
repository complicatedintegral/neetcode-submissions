import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        h = []
        res = []

        for i in range(len(nums)):
            heapq.heappush(h, (-nums[i], i))
            if i >= (k-1):
                # print(h[0])
                while h[0][1] <= (i-k): # i-k gives the wrong window, should be i-k+1
                    heapq.heappop(h)

                res.append(-h[0][0])

        return res