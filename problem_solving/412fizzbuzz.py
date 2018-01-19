def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    fizz_array = []
    for x in range(1,n+1):
        new_val = ""
        if x%3 == 0:
            new_val = "Fizz"
        if x%5 == 0:
            new_val += "Buzz"
        if x%3 != 0 and x%5 != 0:
            new_val = str(x)

        fizz_array.append(new_val)

    return fizz_array

n = 15
p = fizzBuzz(n)
print(p)
