class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # create a maxheap of (dist, points[i]). stop when size becomes k. 
        maxHeap = []
        for i in range(len(points)):
            heapq.heappush(maxHeap, (-(points[i][0]**2 + points[i][1]**2), points[i]))
            if i >= k:
                heapq.heappop(maxHeap)
        return [point[1] for point in maxHeap]
