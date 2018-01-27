class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_counter = 0
        t_counter = 0
        while s_counter < len(s) and t_counter < len(t):
            print("here")
            if s[s_counter] == t[t_counter]:
                s_counter += 1
            t_counter  += 1

        return s_counter == len(s) or len(s) == 0


sol = Solution()
s = "a"
t = ""
res = sol.isSubsequence(s,t)
print(res)
