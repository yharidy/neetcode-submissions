class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_seq = 0
        substr = set()
        l = 0
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l+=1
            substr.add(s[r])
            max_seq = max(max_seq, len(substr))
        return max_seq