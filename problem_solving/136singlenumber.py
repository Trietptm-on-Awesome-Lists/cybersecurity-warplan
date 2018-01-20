def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    new_dic = {}
    for el in nums:
        if el in new_dic:
            new_dic.pop(el)
        else:
            new_dic[el] = 1

    return next(iter(new_dic))

arr = [2,3,4,5,6,2,3,4,5,6,1,1,9]
num = singleNumber(arr)
print(num)
