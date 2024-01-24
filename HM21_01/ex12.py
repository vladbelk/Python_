def calculate_factorials(list_of_integers):
    list_of_factorials = []
    for integer in list_of_integers:
        factorial = 1
        for i in range(1, integer + 1):
            factorial *= i
        list_of_factorials.append(factorial)
    return list_of_factorials
try:
    list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_of_factorials = calculate_factorials(list_of_integers)
    print("Факторіали елементів списку:", list_of_factorials)
except Exception as e:
    print(e)