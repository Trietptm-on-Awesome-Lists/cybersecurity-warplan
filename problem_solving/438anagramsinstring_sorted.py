class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        if p == s:
            return [0]

#         p_dic = {}

#         for e in p:
#             if e in p_dic:
#                 p_dic[e] += 1
#             else:
#                 p_dic[e] = 1

#         print(p_dic)

        p = sorted(p)
        i = 0
        indices_anagram = []
        while (i + len(p)) <= len(s):
            test_array = []
            for n in range(i,i + len(p)):
                test_array.append(s[n])

            test_array.sort()
            if test_array == p:
                indices_anagram.append(i)

            i += 1
        return indices_anagram
