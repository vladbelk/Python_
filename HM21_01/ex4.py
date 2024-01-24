def remove_number(list_of_integers, number):
    count_removed = 0
    while number in list_of_integers:
        del list_of_integers[list_of_integers.index(number)]
        count_removed += 1
    return count_removed
try:
    list_of_integers = [1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6]
    count_removed = remove_number(list_of_integers, 5)
    print("Кількість видалених елементів:", count_removed)
except Exception as e:
    print(e)