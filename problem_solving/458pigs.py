class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # 1000 buckets, we want a unique combination of pigs for each bucket
        # we need 2^10 = 1024 | 10 pigs for unique combination in 1 attempt
        # 000000000 for bucket 0, 00000001 for bucket 1 etc
        # since we have minTest/minDie = 4 tries we can cover 256 values in each attempt
        # if all die end
        # if only one dies,
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
