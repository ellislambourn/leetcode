class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # binary search the numbers not the indices
        l = 1 
        r = len(nums) - 1
        # use the fact that at mid, to the left there should be <= mid elements there.
        while l<r:
            mid = (r+l) //2
            count = sum(1 for num in nums if num <= mid)

            if count > mid:
                r = mid 
            else:
                l = mid + 1
            
        return l
        