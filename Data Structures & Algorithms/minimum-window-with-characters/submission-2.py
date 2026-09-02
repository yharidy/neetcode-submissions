class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0)+1
        res = ""
        min_length = float("Infinity")
        matched = 0
        window = {}
        need =  len(t_count)

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) +1
            if s[r] in t_count and t_count[s[r]]==window[s[r]]:
                matched+=1
            while matched==need:
                if (r-l+1) < min_length:
                    res=s[l:r+1]
                    min_length=r-l+1
                window[s[l]]-=1
                if s[l] in t_count and window[s[l]]<t_count[s[l]]:
                    matched-=1
                l+=1
            r+=1

        return res
                
            