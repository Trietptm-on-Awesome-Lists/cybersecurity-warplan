class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        counting_sum = True
        new_num = num
        my_sum = 0
        while counting_sum:
            my_sum = 0
            for x in str(new_num):
                my_sum += int(x)

            if (my_sum // 10) < 1:
                counting_sum = False
            else:
                new_num = my_sum
        return my_sum
