class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums=sorted(nums)
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while r > l:
                total = nums[i]+nums[r]+nums[l] 
                if total == 0:
                    res.append([nums[i], nums[r], nums[l]])
                    l+=1
                    r-=1
                    while r > l and nums[r]==nums[r+1]:
                        r-=1
                    while r>l and nums[l]==nums[l-1]:
                        l+=1
                elif total < 0:
                    l+=1
                else:
                    r-=1
                
        return res