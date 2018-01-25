def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    col = len(nums[0])
    rows = len(nums)

    if r*c != rows*col:
        return nums
    else:
        new_matrix = []
        i,j = 0,0
        while i < rows and j < col:

            for r1 in range(0,r):
                new_row = []
                for c1 in range(0,c):
                    new_row.append(nums[i][j])
                    j += 1
                    if j == col and i < rows:
                        j = 0
                        i += 1


                new_matrix.append(new_row)



        return new_matrix

nums = [[2,4][5,6]]
r = 1
c = 4
matrixReshape(nums, r, c)
