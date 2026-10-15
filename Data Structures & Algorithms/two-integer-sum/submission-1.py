class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain_to_idx = {}
        for i, n in enumerate(nums):
            if n in remain_to_idx:
                return [remain_to_idx[n], i]
            remain_to_idx[target-n] = i
        