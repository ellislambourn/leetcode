class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        # this is combination sum 1 again but cant visit same candidate[i]
        # this version makes sure duplicates arent included in solution. 

        def dfs(i, curr):
            if curr == target:
                res.append(subset.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                    
                if curr + candidates[j] > target:
                    break
                
                subset.append(candidates[j])
                
                dfs(j+1, curr + candidates[j])
                subset.pop()
                
        dfs(0, 0)
        return res