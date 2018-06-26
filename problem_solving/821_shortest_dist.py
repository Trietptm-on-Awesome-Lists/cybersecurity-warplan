"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:

    S string length is in [1, 10000].
    C is a single character, and guaranteed to be in string S.
    All letters in S and C are lowercase.
"""
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        Ziddy code, should have picked a better approach
        """
        last_find = -1
        dist_arr = []
        for el_idx in range(len(S)):
            if S[el_idx] == C:
                if last_find == -1:
                    val = [x for x in range(el_idx,0,-1)]
                else:
                    diff = el_idx - last_find
                    if diff % 2 == 0:
                        half_way_arr = [x for x in range(1, diff//2)]
                        val = half_way_arr + [diff//2] + half_way_arr[::-1]
                    else:
                        half_way_arr = [x for x in range(1, diff//2 + 1)]
                        val = half_way_arr + half_way_arr[::-1]
                dist_arr += val  + [0]
                last_find = el_idx

        if last_find != len(S):
            dist_arr += [x for x in range(1,len(S) - last_find)]
        return(dist_arr)
sol = Solution()
s = "loveleetcoade"
c = "e"
sol.shortestToChar(s, c)
print([3,2,1,0,1,0,0,1,2,2,1,0,1,2])
