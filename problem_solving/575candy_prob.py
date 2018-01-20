
def distributeCandies(candies):

    num_of_candies = len(candies)//2
    type_of_candies = len(set(candies))
    if type_of_candies >= num_of_candies:
        return num_of_candies
    elif type_of_candies < num_of_candies:
        return type_of_candies

arr = [1,1,2,2,3,3]
res  = distributeCandies(arr)
print(res)

arr = [1,1,1,1]
res  = distributeCandies(arr)

# res = distributeCandies(arr)
print(res)
# [1,1,2,2]
