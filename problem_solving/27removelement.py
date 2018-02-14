class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = 0
        while n < len(nums):
            if nums[n] == val:
                del nums[n]
            else:
                n += 1

        return (len(nums))
