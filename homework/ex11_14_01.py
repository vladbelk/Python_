def sum_of_range(start, end):
    if start > end:
        return None
    sum = 0
    for number in range(start, end + 1):
        sum += number
    return sum

try:
    start = int(input("Введіть початкове число: "))
    end = int(input("Введіть кінцеве число: "))
    sum = sum_of_range(start, end)
    print("Сума чисел у діапазоні:", sum)

except Exception as e:
    print(e)