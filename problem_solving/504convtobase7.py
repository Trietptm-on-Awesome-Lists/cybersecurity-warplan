def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    # print(num)
    # print(num//base)
    base = 7
    if num < base:
        return str(num)

    return convertToBase7(num//base) + str(num%base)


print(convertToBase7(7))
