class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h >= len(piles)
        # if h== len(piles)-> maximum k -> max(piles)
        # solution is in (1, max_k=m)
        # use binary search to find the minimum k given that as k increases, the total time decreases
        l = 1
        r = max(piles)
        k = r
        while r >= l:
            m = (l+r)//2
            hours = 0
            for p in piles:
                hours +=math.ceil(p/m)
            if hours <= h:
                r = m-1
                k = min(k, m)
            else:
                l = m +1
        return int(k)

            
            