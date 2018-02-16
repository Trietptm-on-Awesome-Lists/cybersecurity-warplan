class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if s == t:
            return True
        if len(s) != len(t):
            return False

        s_dic = {}
        for e in s:
            if e in s_dic:
                s_dic[e] += 1
            else:
                s_dic[e] = 1

        t_dic = {}
        for e in t:
            if e in t_dic:
                t_dic[e] += 1
            else:
                t_dic[e] = 1
        res = True
        for v in t_dic:
            if v not in s_dic or t_dic[v] != s_dic[v]:
                res = False
                break
        return res
