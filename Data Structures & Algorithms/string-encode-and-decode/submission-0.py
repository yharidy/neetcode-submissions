class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += str(l)+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            cnt = int(s[i:j])
            res.append(s[j+1:j+1+cnt])
            i = j+1+cnt
        return res

