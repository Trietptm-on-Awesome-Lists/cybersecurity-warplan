def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        count = 0
    elif n == 3:
        count = 1
    else:
        count = 1
        primes = []
        for x in range(3,n,2):
            is_prime = True
            for p in primes:
                if x%p == 0:
                    is_prime = False
                    break
                if p > .5*x:
                    break
            if is_prime:
                primes.append(x)
                count += 1

    return count

res = countPrimes(8)
print(res)
