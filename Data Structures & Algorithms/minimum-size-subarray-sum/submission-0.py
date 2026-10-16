class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        subarr = []
        currSum = 0
        res = 0
        for r in range(len(nums)):
            subarr.append(nums[r])
            currSum+=nums[r]
            while currSum >= target:
                if res == 0:
                    res = len(subarr)
                else:
                    res = min(res, len(subarr))
                currSum -=subarr[0]
                subarr.pop(0)
        return res


        