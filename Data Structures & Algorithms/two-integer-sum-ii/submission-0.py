class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = {}
        for i, num in enumerate(numbers):
            if num in complement:
                return [complement[num]+1, i+1]
            complement[target-num] = i
        
        