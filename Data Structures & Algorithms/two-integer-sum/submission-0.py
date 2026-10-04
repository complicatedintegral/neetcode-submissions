class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = dict()
        for i,j in enumerate(nums): # i is index, j is value
            v = target - j
            if v in d:
                return [d[v], i]
            d[j] = i
