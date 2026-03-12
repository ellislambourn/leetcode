class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(subset.copy())
                return
            
            # include i
            subset.append(nums[i])
            total += nums[i]
            dfs(i, total)
            
            # dont include i

            subset.pop()
            total -= nums[i]
            dfs(i+1, total)
        dfs(0,0)
        return res