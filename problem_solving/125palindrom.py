class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_of_string = len(s)

        approved = {}
        for i in range(0,10 ):
            approved[str(i)] = True

        for i in range(ord('a'),ord('z')):
            approved[chr(i)] = True
            approved[chr(i).upper()] = True

        in_process = True
        j = len_of_string - 1 # last character
        i = 0
        # print(approved)
        is_pal = True

        while j > i:

            while s[i] not in approved and i < (len_of_string - 1):
                i += 1
            while j > i and s[j] not in approved:
                j -= 1

            if j <= i:
                break
            # print("Compared %s with %s"%(s[i],s[j]))
            if s[i].lower() != s[j].lower():
                is_pal = False
                break
            else:
                i += 1
                j -= 1


        return is_pal
