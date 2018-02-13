def countPrimeSetBits(self, L, R):
    """
    :type L: int
    :type R: int
    :rtype: int
    """
    L_bin = bin(L)[2:][::-1]
    R_bin = bin(R)[2:][::-1]
    diff_in_len = len(L_bin) - len(R_bin)

    if diff_in_len < 0:
        small, big = L_bin, R_bin
    else:
        small, big = R_bin, L_bin

    small = small[:2] + "0"*abs(diff_in_len) + small[2:]

    counter = 0
    for i in range(0,(len(big))):
        if small[i] != big[i]:
               counter = counter + 1


    return counter


start = "0000"

# 1 to 0, shift to right
while start != "1111":

    if start[len(start) - 1] == '0':
        start = start[:-1] + '1'
    else:
        start = start[:-1] + '0'
        counter = len(start) - 2
        while counter != -1:
            if start[counter] == '1':
                start = start[:counter] + '0' + start[counter + 1:]
            else:
                start = start[:counter] + '1' + start[counter + 1:]
                break
            counter = counter - 1
    print(start)
