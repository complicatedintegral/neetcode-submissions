class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = 1
        fod = [] # first order differencing 

        while j < len(prices):
            fod.append(prices[j]-prices[i])
            i += 1
            j += 1

        s = 0
        ms = 0 # max value of s
        for k in fod:
            if (s + k) >= 0:
                s += k  
            else:
                s = 0
            ms = max(s, ms)
            
        return ms