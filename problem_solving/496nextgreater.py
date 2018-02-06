def next_greater(nums1,nums2)
        sorted_num2 = nums2
        num2_dic = {}
        for i in range(0,len(sorted_num2)):
            has_greater = -1
            for j in range(i,len(sorted_num2)):
                if sorted_num2[j] > sorted_num2[i]:
                    has_greater = sorted_num2[j]
                    break

            num2_dic[sorted_num2[i]] = has_greater

        new_arr = []
        for num in nums1:
            new_arr.append(num2_dic[num])

        return new_arr
