class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_of_nums = sum(nums)
        len_of_nums = len(nums)
        print(sum_of_nums, len_of_nums)
        num_of_zeroes = len_of_nums - sum_of_nums
        count = 0
        max_count = -1
        if num_of_zeroes == 0:
            return len_of_nums
        else:
            for x in range(0,len(nums)):

                if nums[x] == 1:
                    count += 1
                else:
                    if count > max_count:
                        max_count = count
                    count = 0
            if count > max_count:
                max_count = count

        return max_count
