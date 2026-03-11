class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # binary bitwise
        res = []
        for mask in range(1 << len(nums)): # 2 raised to len(nums)
            subset = []
            for j in range(len(nums)):
                if mask & (1 << j):
                    subset.append(nums[j])
            res.append(subset)
        return res
            