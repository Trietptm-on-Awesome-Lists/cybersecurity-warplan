def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    # diff = 0
    # i = 0
    # while i < len(prices):
    #     print(i)
    #     min_price = prices[i]
    #     for j in range(i + 1,len(prices)):
    #         if prices[j] < min_price:
    #             # print("did %i" %(i))
    #             i = j
    #             break
    #         elif diff < prices[j] - min_price:
    #             diff = prices[j] - min_price
    #     i += 1
    # return diff
    """
    Time complexity is O(N)
    Space complexit is O(1),
    removed the new array dont need it
    :type prices: List[int]
    :rtype: int
    """
    max_diff = float("-inf")
    if len(prices) < 1:
        return 0

    base = prices[0]
    for i in range(0,len(prices)):

        diff = prices[i] - base

        if diff < 0:
            base = prices[i]
            diff = 0

        if diff > max_diff:
            max_diff = diff

    return max_diff

# arr = [7, 5, 1, 3,1,1, 6, 1]
# arr = [2,4,1]
    # [0, -2, -6, -4, -1, -6]
# arr = [7, 6, 4, 3, 1]
# arr = [1,0]
# arr = []
res = maxProfit(arr)
print(res)
