class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o','u']

        S = S.split(' ')
        for word_idx in range(len(S)):
            if S[word_idx][0].lower() in vowels:
                S[word_idx] += 'ma'
            else:
                S[word_idx] = S[word_idx][1:] + S[word_idx][0] + 'ma'
            S[word_idx] += 'a'*(word_idx+1)

        return(" ".join(S))


S =  "I speak Goat Latin"

sol = Solution()
ans = sol.toGoatLatin(S)
print(ans)
