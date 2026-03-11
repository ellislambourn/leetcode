class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # binary bitwise
        res = []
        for i in range(2**len(nums)):
            binary = format(i, f"0{len(nums)}b")
            subset = []
            for j in range(len(nums)):
                if int(binary[len(nums) - j-1]):
                    subset.append(nums[j])
            res.append(subset)
        return res
            