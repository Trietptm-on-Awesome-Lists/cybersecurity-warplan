class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = float('-inf')

        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2 and n < max1:
                max3 = max2
                max2 = n
            elif n > max3 and n < max2:
                max3 = n


        if max3 == float('-inf'):
            max3 = max1

        return max3
