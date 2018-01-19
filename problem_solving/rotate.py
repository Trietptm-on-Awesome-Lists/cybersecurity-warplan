def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if abs(k) > len(nums):
        k = k%len(nums)
    if k != 0:
        nums[:k],nums[k:] = nums[-k:], nums[:-k]
    return (nums)
 # n = 7 and k = 3, the array [1,2,3,4,5,6,7]

arr = [1,2,3,4,5,6,7]
arr = [-1]
k = 2
print(rotate(arr, k))
