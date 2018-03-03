class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sin_num = None
        for x in range(0,len(nums) - 1):
            if nums[x] != nums[x+1]:
                sin_num = nums[x + 1]

        return sin_num
