class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for e in s.split(' '):
            if e:
                count += 1
        return(count)
