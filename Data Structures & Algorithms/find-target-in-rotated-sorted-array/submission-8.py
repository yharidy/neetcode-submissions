class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        res =-1
        while l<r:
            m = (l+r)//2
            if nums[m]> nums[r]:
                l = m+1
            else:
                r = m
            
        pivot = l
        if target == nums[pivot]:
            return l
        if target <= nums[-1]:
            start = pivot
            end = len(nums)-1
        else:
            start = 0
            end = pivot -1
        while start<=end:
            m = (start+end)//2
            if nums[m]==target:
                res = m
                break
            if nums[m]>target:
                end = m-1
            else:
                start = m+1
        return res
