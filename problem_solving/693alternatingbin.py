def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    n_bin = bin(n)[2:]

    for i in range(0,len(n_bin) - 1):
        if int(n_bin[i])^int(n_bin[i+1]) == 0:
            return False

    return True

print(hasAlternatingBits(7))
