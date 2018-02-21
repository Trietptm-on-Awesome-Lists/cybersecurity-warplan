class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        alph = {}
        for x in range(ord('a'),ord('z') + 1):
            alph[chr(x)] = chr(x).upper()
            alph[chr(x).upper()] = chr(x)

        possible_vals = []
        possible_vals.append(S)

        def all_possibilites(constant,S):

            for ch_index in range(0,len(S)):
                if S[ch_index] in alph:
                    possible_vals.append(constant + S[:ch_index] + alph[S[ch_index]] + S[ch_index+1:])
                    all_possibilites(constant + S[:ch_index] + alph[S[ch_index]], S[ch_index+1:])

        all_possibilites("",S)
        return(possible_vals)
