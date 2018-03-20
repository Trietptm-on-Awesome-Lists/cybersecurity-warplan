class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last_pos = {val: index for index, val in enumerate(S)}

        min_len = -1
        division_array = []
        last_index = 0
        for x_i in range(0,len(S)):

            last_pos_index = last_pos[S[x_i]]

            if last_pos_index > min_len:
                min_len = last_pos_index

            if x_i == min_len:
                division_array.append(min_len + 1 - last_index)
                last_index = min_len + 1
                min_len = -1

        return(division_array)
