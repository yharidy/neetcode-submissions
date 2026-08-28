class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_freq = {}
        for c in s:
            s_freq[c] = s_freq.setdefault(c,0) + 1
        t_freq = {}
        for c in t:
            t_freq[c]= t_freq.setdefault(c,0) + 1
        
        return t_freq==s_freq