# Fix this, make efficient
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        num_of_rows = len(matrix)
        num_of_col = len(matrix[0])# always 1 col constraint

        diagonal = True
        last_element = num_of_col
        for i in range(0,num_of_rows - 1):
            for j in range(0, last_element):

                counter = 1
                while diagonal is True and (j + counter) < num_of_col  and (i + counter) < num_of_rows:
                    print(matrix[i][j], matrix[i+1][j+1])
                    if matrix[i][j] != matrix[i+counter][j+counter]:
                        diagonal = False

                    counter += 1
                if diagonal == False:
                    return(diagonal)

            last_element = i + 1



sol = Solution()
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
sol.isToeplitzMatrix(matrix)


# 1234
# 5123
# 9512
