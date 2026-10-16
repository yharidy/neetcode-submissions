class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sorted_nums = sorted(nums)
        max_cons = 1
        cons = 1
        prev = sorted_nums[0]
        for n in sorted_nums[1:]:
            if n-prev==1:
                cons+=1
            elif n-prev==0:
                pass
            else:
                max_cons=max(max_cons, cons)
                cons=1
            prev = n
        max_cons=max(max_cons, cons)
        return max_cons
