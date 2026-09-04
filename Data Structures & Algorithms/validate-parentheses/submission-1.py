class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["{", "(", "["]
        matches = {
            '}': '{',
            ')': '(',
            ']':'['
        }
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            elif stack and stack[-1] == matches[c]:
                stack.pop()
            else:
                return False
        return not stack