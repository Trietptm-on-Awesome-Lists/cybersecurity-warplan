def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    # Brute force
    number = sum(s in J for s in S)
    return number
