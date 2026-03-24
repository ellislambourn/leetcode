class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        removed = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                removed.append(i)
        while removed:
            nums.pop(removed.pop())
        return len(nums)