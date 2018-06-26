"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        last_substr = ""
        un_substr = ""
        i = 0
        while i < len(s):
            if s[i] not in un_substr:
                un_substr += s[i]
            else:
                i = i - len(un_substr) + 1
                if len(un_substr) >  len(last_substr):
                    last_substr = un_substr
                un_substr = s[i]
            i += 1
        if len(un_substr) >  len(last_substr):
            last_substr = un_substr
        return len(last_substr)

sol = Solution()
sol.lengthOfLongestSubstring("dvdf")
