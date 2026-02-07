class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we can use a set "found" this is O(n) space and time
        found = set()
        for num in nums:
            if num in found:
                return num
            found.add(num)