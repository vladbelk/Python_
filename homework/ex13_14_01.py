def is_happy_number(number):
    first_three_digits = number // 1000
    last_three_digits = number % 1000

    first_three_digits_sum = sum(int(digit) for digit in str(first_three_digits))

    last_three_digits_sum = sum(int(digit) for digit in str(last_three_digits))

    return first_three_digits_sum == last_three_digits_sum

try:
    number = int(input("Введіть число: "))

    is_happy = is_happy_number(number)

    print("Число", number, "є щасливим:", is_happy)

except Exception as e:
    print(e)