class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h >= len(piles)
        # if h== len(piles)-> maximum k -> max(piles)
        # solution is in (1, max_k=m)
        # use binary search to find the minimum k given that as k increases, the total time decreases
        l = 1
        r = max(piles)
        res = r
        
        while l<=r:
            m = (l+r)//2
            total = 0
            for n in piles:
                total+=math.ceil(n/m)
            if total > h:
                l=m+1
            else:
                res = min(res, m)
                r = m-1
        return res
