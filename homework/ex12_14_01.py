def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

try:
    number = int(input("Введіть число: "))
    is_prime = is_prime(number)
    print("Число", number, "є простим:", is_prime)

except Exception as e:
    print(e)