def matrix_transpose(input_string,columns, force_fit=True, return_matrix=False):
    """
    gives transpose of matrix
    args:
        input_string: string to be converted into a matrix
        colums: number of columns to divide string into
        force_fit: Add characters to create column
        return_matrix: If true, returns a matrix form, else sentence
    resule:
        transpose of the matrix
    """
    try:

        remainder = len(input_string)%columns
        if remainder != 0:
            if force_fit:
                extra = columns - remainder
                input_string = input_string + "-"*extra
            else:
                raise Exception("Can't fit values into this matrix")



        converted_matrix = [input_string[c-columns:c] for c in range(columns,len(input_string) + 1,columns)]
        rows = len(converted_matrix)

        transposed_matrix_array = [converted_matrix[row][i]  for i in range(0,columns) for row in range(0,len(converted_matrix))]

        if return_matrix:
            return [transposed_matrix_array[x - rows:x] for x in range(rows,len(transposed_matrix_array) + 1,rows)]

        return "".join(transposed_matrix_array)

    except Exception ,e:
        return "[*] Exception " + str(e)

print(matrix_transpose("HEYALICEHOWYOUDOINGA",4))
print(matrix_transpose("HEYALICEHOWYOUDOING",3, force_fit=False))
print(matrix_transpose("HEYALICEHOWYOUDOING",3, return_matrix=True))
