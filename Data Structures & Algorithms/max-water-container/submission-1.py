class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        n = len(heights)
        r = n-1
        max_area = 0
        area = 0
        while r > l:
            area = (r-l) * min(heights[l], heights[r])
            max_area = max(max_area, area)
            if heights[l] <= heights[r]:
                l+=1
            else: 
                r-=1
        return max_area


        