class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heap where we pop twice and heappush the differenec of the two popped items. do while len(heap) > 1.
        stones = [-weight for weight in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            out1, out2 = heapq.heappop(stones), heapq.heappop(stones)
            diff = abs(out1 - out2)
            if diff > 0:
                heapq.heappush(stones, -diff)
        return -stones[0] if stones else 0 