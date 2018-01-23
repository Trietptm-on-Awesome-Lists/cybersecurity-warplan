def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    number_map = {}
    #O(1)
    for i in range(0,10):
        number_map[str(i)] = i


    num_arr_str = [num1, num2]
    num_arr_int = []
    for num1 in num_arr_str:
        num1_int = 0
        num1_len = len(num1) - 1

        for x in range(0,len(num1)):
            multi = 10**num1_len
            num1_int += multi*number_map[num1[x]]
            num1_len -= 1

        num_arr_int.append(num1_int)

    return str(sum(num_arr_int))


sum_val = addStrings("123","999")
print(sum_val)
