class Solution(object):

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # there can be only one element out of order
        counter = 0
        sorted_arrays = []
        off_index = 0
        response = False

        #Worst case Time O(N)
        for i in range(0,len(nums) - 1):

                if nums[i] > nums[i+1]:
                    counter += 1
                    off_index = i + 1
                    sorted_arrays.append(nums[:off_index])

                # if more than two errors
                if counter >= 2:
                    break

        if counter == 0: # if list was sorted
            response = True
        elif counter == 1: # if there was only one hiccup
            # Divided into two arrays
            sorted_arrays.append(nums[off_index:])
            print(sorted_arrays)
            min_array = sorted_arrays[0]
            max_array = sorted_arrays[1]

            # if only one element, can be moved arround
            if len(min_array) == 1 or len(max_array) == 1:
                response = True
            # if second last element in first array is less than min element
            # of the second array
            elif min_array[-1] != min_array[-2] and min_array[-2] <= max_array[0]:
                response = True
            # if max of first array is less than second element of
            #the second array
            elif max_array[0] != max_array[1] and max_array[1] >= min_array[-1]:
                response = True

        return response



rand_array = []
rand_array.append([-5, -4, 0, 0, -3, 1, 2, 3, 4, 5])
rand_array.append([1, 2, 3, 4, 5, 6, 7, 1, 9, 10])
rand_array.append([1,2,3,0])
rand_array.append([4,5,1,2,3])
rand_array.append([1,1,1,2,1,1,1])
rand_array.append([1,1,1,1,1,1])
rand_array.append([1,1,1,1,5,1,2,3])

rand_array.append([0, 0, 0, 0, 0, 1, 1, 1, 3,  1, 1])
rand_array.append([3,4,2,3])
rand_array.append([4,5,1,2,3])
rand_array.append([1, 2, 3, 4, 5, 6, 7, 1, 9, 10])
rand_array.append([1, 2, 3, 4, 5, 6, 7, 1, 9, 11, 12, 15])
rand_array.append([4,5,2,6,7])
rand_array.append([4,2,3])

for rand in rand_array:
    sol = Solution()
    ans = sol.checkPossibility(rand)
    print(ans)


# 1 2 3 4 5 1 2 3 4 5
# 1 2 3 4 10 5 6 7 8
