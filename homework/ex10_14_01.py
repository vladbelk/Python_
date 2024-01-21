def max_of_four(a, b, c, d):
    if a > b:
        largest = a
    else:
        largest = b

    if largest < c:
        largest = c

    if largest < d:
        largest = d

    return largest

try:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    c = int(input("Введіть третє число: "))
    d = int(input("Введіть четверте число: "))

    largest = max_of_four(a, b, c, d)

    print("Найбільше число:", largest)

except Exception as e:
    print(e)