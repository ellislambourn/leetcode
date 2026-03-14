class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def rec(visited):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if visited & (1 << i): # if this bit is active
                    continue
                
                subset.append(nums[i])
                visited = visited | (1 << i) # include this bit

                rec(visited)
                
                subset.pop()
                visited &= ~(1 << i) #remove this bit
            
        rec(0)

        return res