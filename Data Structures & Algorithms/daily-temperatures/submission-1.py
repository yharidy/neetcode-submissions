class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0]< t:
                idx_to_insert = stack[-1][1]
                res[idx_to_insert] = i-idx_to_insert
                stack.pop(-1)
            stack.append((t,i))
        return res

        