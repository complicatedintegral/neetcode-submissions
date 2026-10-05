import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)

            if a != b:
                heapq.heappush(stones, -abs(a-b))

            # print(stones)

        if len(stones) == 1:
            return -stones[0]
        else: return 0