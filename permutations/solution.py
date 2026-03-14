class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visited = set() # can replace for a dictionary of {num : T/F}

        def rec(length):
            if length == len(nums):
                res.append(subset.copy())
                return

            for num in nums:
                if num in visited:
                    continue
                
                subset.append(num)
                visited.add(num)

                rec(length + 1)
                
                subset.pop()
                visited.discard(num)
        rec(0)
        return res