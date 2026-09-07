class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = []
        r = []
        stack = []
        for i in range(len(heights)):
            if i ==0:
                stack.append((i, heights[i]))
                l.append(0)
                continue
            while stack and stack[-1][1]>=heights[i]:
                stack.pop()
            left_boundary = 0 if not stack else stack[-1][0]+1
            l.append(left_boundary)
            stack.append((i,heights[i]))
        
        stack = []
        for i in range(len(heights)-1, -1, -1):
            if i== len(heights)-1:
                r.append(i)
                stack.append((i, heights[i]))
                continue
            while stack and stack[-1][1]>=heights[i]:
                stack.pop()
            right_boundary = len(heights)-1 if not stack else min(len(heights)-1,stack[-1][0]-1)
            r.append(right_boundary)
            stack.append((i, heights[i]))
        
        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i] * (r[len(heights)-i-1]-l[i]+1))
        return max_area
    

