from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # i want frequencies of all the tasks.
        freqs = [-val for val in Counter(tasks).values()] # this is a list of (3,2,2), frequencies of each task
        # i want to make freqs a maxheap so the most common task is always done.
        heapq.heapify(freqs)
        q = deque() # structure (freq, time available) so the front item will only be popped when time available = res.


        res = 0 # the clock
        while freqs or q:
            res+=1
            
            if not freqs:
                res = q[0][1]
            else:
                cnt = 1 + heapq.heappop(freqs)
                if cnt:
                    q.append([cnt, res + n])
            if q and q[0][1] == res:
                heapq.heappush(freqs, q.popleft()[0])
        return res


