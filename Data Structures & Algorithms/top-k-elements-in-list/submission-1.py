class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0)+1
        res = []
        freq = {f: [] for f in count.values()}
        for c, f in count.items():
            freq[f].append(c)
        for i in range(len(nums), 0, -1):
            if i in freq:
                res.extend(freq[i])
                if len(res)==k:
                    return res
