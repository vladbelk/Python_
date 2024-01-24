def reverse_list(list_of_integers):
    reversed_list = []
    for integer in list_of_integers[::-1]:
        reversed_list.append(integer)

    return reversed_list
try:
    list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reversed_list = reverse_list(list_of_integers)
    print("Перевернутий список:", reversed_list)
except Exception as e:
    print(e)