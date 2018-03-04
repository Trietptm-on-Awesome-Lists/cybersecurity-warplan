class Solution(object):
    def singleNonDuplicate(self, list):
        """
        :type nums: List[int]
        :rtype: int
        """
        # go to the middle
        # if next is same, then upper half
        # if next is else, then lower half
#         num_len = len(nums)

#         def bin_search(our_nums):
#             mid = (len(our_nums) + 1)/2 - 1
#             print(our_nums, len(our_nums), mid)


#             if len(our_nums) <= 3:
#                 if len(our_nums) < 1 :
#                     sin_num = 0
#                 elif len(our_nums) == 1:
#                     sin_num = our_nums[0]
#                 else:
#                     if our_nums[mid] == our_nums[mid + 1]:
#                         sin_num = our_nums[mid - 1]
#                     else:
#                         sin_num = our_nums[mid + 1]
#                 return sin_num

#             if our_nums[mid] != our_nums[mid + 1] and our_nums[mid] != our_nums[mid - 1]:
#                 sin_num = our_nums[mid]
#                 return sin_num

#             if (mid + 1)%2 == 0:
#                 if our_nums[mid] != our_nums[mid + 1]:
#                     sin_num = bin_search(our_nums[mid + 1:])
#                 else:
#                     sin_num = bin_search(our_nums[0:mid - 1])
#             else:
#                 if our_nums[mid] == our_nums[mid + 1]:
#                     sin_num = bin_search(our_nums[mid + 1:])
#                 else:
#                     sin_num = bin_search(our_nums[0:mid - 1])

#             return sin_num
#         sin_num = bin_search(nums)
#         return (sin_num)
        low, high = 0 , len(list)-1
        while (low<high):
            mid = low + (high - low)/2
            if (list[mid] != list[mid+1] and list[mid]!=list[mid-1]):
                return list[mid]
            elif (mid%2 ==1 and list[mid]==list[mid-1]):
                low = mid + 1
            elif (mid%2 == 0 and list[mid]==list[mid+1]):
                low = mid + 1
            else:
                high = mid - 1
        return list[low]
