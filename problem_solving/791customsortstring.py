class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        pos_in_S = {}

        for x in range(0,len(S)):
            pos_in_S[S[x]] = x

        pos_in_T = {}

        not_rel = ""

        for x in range(0,len(T)):
            if T[x] in pos_in_T:
                pos_in_T[T[x]] += 1
            else:
                if T[x] not in pos_in_S:
                    not_rel += T[x]
                else:
                    pos_in_T[T[x]] = 1

        sorted_array = ""
        for i in S:
            if i in pos_in_T:
                sorted_array += i * pos_in_T[i]


        return sorted_array + not_rel
