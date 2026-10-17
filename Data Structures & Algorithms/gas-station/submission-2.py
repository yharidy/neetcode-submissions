class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n = len(gas)
        # for i in range(n):
        #     tank = gas[i] - cost[i]
        #     if tank < 0:
        #         continue
        #     j = (i+1)%n
        #     while j != i:
        #         tank += gas[j]
        #         tank -= cost[j]
        #         if tank < 0:
        #             break
        #         j+=1
        #         j%=n
        #     if i == j:
        #         return i
        # return -1
        n = len(gas)
        start = n-1
        end = 0
        tank = gas[start]-cost[start]
        while start > end:
            if tank < 0:
                start-=1
                tank+=gas[start]-cost[start]
            else:
                tank+=gas[end]-cost[end]
                end+=1

        if tank >= 0:
            return start
        return -1