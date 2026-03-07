class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a minheap of k size and return the smallest element in that minheap.
        minheap = []
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(minheap, nums[i])
            elif minheap[0] < nums[i]:
                heapq.heappush(minheap, nums[i])
                heapq.heappop(minheap)
        return minheap[0]

        # could do quickselect but i do not know how to code the algorithm just yet.
                