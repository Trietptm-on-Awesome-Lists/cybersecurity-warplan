def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    Time O(N)
    Space O(N)
    """
    for i in range(0,num + 1):
        print(list(bin(i)[2:]).count("1"),bin(i)[2:], i)
        # print(2**i)


countBits(50)
