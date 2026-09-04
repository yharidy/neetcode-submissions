class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a max heap to keep track of maximum
        # heap = []
        # output = []
        # for i in range(len(nums)):
        #     heapq.heappush(heap, (-nums[i],i))
        #     if i >= k-1:
        #         while heap[0][1] <= i-k:
        #             heapq.heappop(heap)
        #         output.append(-heap[0][0])
        # return output

        # use a dequeue
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            
            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output
                


