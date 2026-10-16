class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        for n in nums_set:
            if n-1 not in nums_set:
                seq_len = 1
                while n+1 in nums_set:
                    seq_len+=1
                    n+=1
                best = max(best, seq_len)
        return best

