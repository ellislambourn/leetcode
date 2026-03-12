class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #  sorted version so i can optimise and not checki larger numbers when total > target.
        res = []
        subset = []
        nums.sort()

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target: # the rest of the list wont work either
                    return
                subset.append(nums[j])
                dfs(j, total + nums[j])
                subset.pop()

        dfs(0,0)
        return res