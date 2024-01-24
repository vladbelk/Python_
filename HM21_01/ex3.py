def count_primes(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [x for x in lst if is_prime(x)]
    return len(primes)
try:
    lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,]
    num_primes = count_primes(lst)
    print(f"Кількість простих чисел у списку: {num_primes}")
except Exception as e:
    print(e)

