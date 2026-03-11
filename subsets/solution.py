class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking dfs
        res = []
        subset = [] 

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include the current item 
            subset.append(nums[i])
            dfs(i+1)

            # dont include the current item
            subset.pop()
            dfs(i+1)
        dfs(0)

        return res
            