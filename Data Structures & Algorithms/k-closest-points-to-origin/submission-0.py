import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        l = []
        for i, j in points:
            d = math.sqrt(i**2 + j**2)
            l.append([d, i, j])

        heapq.heapify(l)
        res = []

        while k > 0:
            d, i, j = heapq.heappop(l)
            res.append([i, j])
            k -= 1

        return res