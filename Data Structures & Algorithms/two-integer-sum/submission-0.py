class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in val_to_index:
                return [val_to_index[diff], i]
            val_to_index[n] = i