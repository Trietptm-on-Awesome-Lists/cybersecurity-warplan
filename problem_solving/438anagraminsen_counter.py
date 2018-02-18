from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        c = Counter(p)
        anagram_indices = []
        window = None
        first_val = None
        for i in range(0, len(s) - len(p) + 1):
            if window is None:
                window = Counter(s[i:i + len(p)])
            else:
                res = window[first_val] - 1
                if res == 0:
                    del window[first_val]
                else:
                    window[first_val] = res

                if s[i + len(p) - 1] not in window:
                    window[s[i + len(p) - 1]] = 1
                else:
                    window[s[i + len(p) - 1]] += 1

            first_val = s[i]
            if c == window:
                anagram_indices.append(i)

        return(anagram_indices)
