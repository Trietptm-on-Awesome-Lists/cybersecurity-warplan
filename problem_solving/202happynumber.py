class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        my_sum = 0
        is_same = {}
        is_not_one = True
        while is_not_one:
            my_sum = 0
            for x in str(n):
                my_sum += int(x)**2

            print(my_sum)
            if my_sum == 1:
                return True
            elif my_sum in is_same:
                return False
            else:
                is_same[my_sum] = True
                n = my_sum
