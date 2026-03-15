class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = [] 
        subset = []
        subsets = []

        def dfs(i):
            nonlocal subset
            if i >= len(nums):
                subsets.append(tuple(sorted(subset))) # this is o(nlogn) and solutions gonna be exponential anyways so might as well just do this.
                # im aware that this will be repeated lots of times.
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop() 
            dfs(i+1)

        dfs(0)
        res = [list(subset) for subset in set(subsets)] # builds expected list list int
        
        return res