class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = 0
        count = 0
        while n < len(nums):
            if nums[n] == 0:
                del nums[n]
                count += 1
            else:
                n += 1

        for i in range(0,count):
            nums.append(0)
