class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find turning point
        l = 0
        r = len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]> nums[r]:
                l = m+1
            else:
                r = m
        pivot = l
        if target > nums[-1]:
            l = 0
            r = pivot-1
        else:
            l = pivot
            r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]< target:
                l = m+1
            else:
                r = m-1
        return -1


