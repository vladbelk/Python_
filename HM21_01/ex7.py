def calculate_sum(list_of_integers):
    return sum(list_of_integers)
try:
    list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_of_integers = calculate_sum(list_of_integers)
    print("Сума елементів списку:", sum_of_integers)
except Exception as e:
    print(e)