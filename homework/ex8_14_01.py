def print_odd_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
            print(i)

try:
    start = int(input("Введіть початкове число: "))
    end = int(input("Введіть кінцеве число: "))
    print_odd_numbers(start, end)

except Exception as e:
    print(e)