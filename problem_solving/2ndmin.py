
min_1, min_2 = float("inf"),float("inf")

y = [1,2,3,4,5,-1,6,7]

for x in y:
    if x < min_1:
        min_2 = min_1
        min_1 = x
    elif x < min_2:
        min_2 = x


print(min_2)
print(min_1)
