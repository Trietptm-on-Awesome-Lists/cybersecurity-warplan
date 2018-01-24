def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # binary search
    max_val = 0
    min_val = len(nums)
    print(nums)
    mid_point = (max_val + min_val) // 2
    if target == nums[mid_point]:
        return mid_point

    if len(nums) < 2:
        if target < nums[mid_point]:
            return mid_point
        else:
            return mid_point + 1

    if target > nums[mid_point]:
        return mid_point + searchInsert(nums[mid_point:],target)
    else:
        return searchInsert(nums[:mid_point],target)

n, t = [1,3,5,6,9,11,13], -1
res = searchInsert(n, t)
print(res)
