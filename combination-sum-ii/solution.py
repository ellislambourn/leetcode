class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        # this is combination sum 1 again but cant visit same candidate[i]

        def dfs(i, curr):
            if i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if curr + candidates[j] > target:
                    return
                subset.append(candidates[j])
                if curr + candidates[j] == target and subset not in res:
                    res.append(subset.copy())
                dfs(j+1, curr + candidates[j])
                subset.pop()
                
        dfs(0, 0)
        return res