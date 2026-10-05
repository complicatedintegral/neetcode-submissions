import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mh = nums # min heap
        self.k = k
        heapq.heapify(self.mh)
        while len(self.mh) > k:
            heapq.heappop(self.mh)
        # print(self.mh)


    def add(self, val: int) -> int:
        heapq.heappush(self.mh, val)
        if len(self.mh) > self.k:
            heapq.heappop(self.mh)
        # print(self.mh)
        return self.mh[0]
