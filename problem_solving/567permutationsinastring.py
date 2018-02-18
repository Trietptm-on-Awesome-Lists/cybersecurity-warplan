from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c = Counter(s1)

        window = None
        first_val = None
        anagram_indices = []
        is_permutation = False
        for i in range(0, len(s2) - len(s1) + 1):
            if window is None:
                window = Counter(s2[i:i + len(s1)])
            else:
                res = window[first_val] - 1
                if res == 0:
                    del window[first_val]
                else:
                    window[first_val] = res

                if s2[i + len(s1) - 1] not in window:
                    window[s2[i + len(s1) - 1]] = 1
                else:
                    window[s2[i + len(s1) - 1]] += 1

            first_val = s2[i]
            if c == window:
                is_permutation = True
                break

        return is_permutation
