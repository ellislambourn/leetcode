class MedianFinder:

    def __init__(self):
        self.lowerHeap = [] #maxheap
        self.higherHeap = [] #minheap
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1
        if self.isOdd(): # add to lower
            if self.higherHeap and num > self.higherHeap[0]:
                transfer = heapq.heappop(self.higherHeap)
                heapq.heappush(self.lowerHeap, -transfer)
                heapq.heappush(self.higherHeap, num)
    
            else:
                heapq.heappush(self.lowerHeap, -num)
        else: # add to higher
            if num < -self.lowerHeap[0]:
                transfer = heapq.heappop(self.lowerHeap)
                heapq.heappush(self.higherHeap, -transfer)
                heapq.heappush(self.lowerHeap, -num)
            else:
                heapq.heappush(self.higherHeap, num)
         

    def findMedian(self) -> float:
        if self.isOdd():
            return float(-self.lowerHeap[0])
        return (-self.lowerHeap[0] + self.higherHeap[0]) /2
        
    def isOdd(self):
        return self.length % 2 == 1