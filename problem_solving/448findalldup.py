class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # print(nums)
        # n = len(nums)
        # expected_sum = n*(1 + n)//2
        # actual_sum = sum(nums)
        # print(actual_sum)
        # print(expected_sum)
        for n in nums:
            nums[abs(n) - 1] = - abs(nums[abs(n) - 1])

        return ([i + 1 for i in range(len(nums)) if nums[i] > 0])
