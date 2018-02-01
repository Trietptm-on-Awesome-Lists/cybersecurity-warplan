def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counter = 0
    max_counter = 0
    for x in nums:
        if x == 1:
            counter += 1
        else:
            if counter > max_counter:
                max_counter = counter
            counter = 0

    if counter > max_counter:
        max_counter = counter

    return max_counter
