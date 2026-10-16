class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        counts = {}
        res = []
        for num in nums:
            counts[num] = counts.get(num,0)+1
        
        n = len(nums)
        for i in range(n):
            counts[nums[i]]-=1
            if i >0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n):
                counts[nums[j]]-=1
                if j-1 > i and nums[j]==nums[j-1]:
                    continue
                
                diff = -(nums[i]+nums[j])
                if counts.get(diff,0)>0:
                    res.append([nums[i], nums[j], diff])
            for j in range(i+1, n):
                counts[nums[j]]+=1
        return res







        