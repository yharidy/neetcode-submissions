class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        curr = []
        for b in s:
            if b in close_to_open:
                if len(curr)==0 or curr[-1]!=close_to_open[b]:
                    return False
                curr.pop(-1)
                continue
            curr.append(b)
        return len(curr)==0