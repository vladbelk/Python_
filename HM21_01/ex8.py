def find_maximum(list_of_integers):
    return max(list_of_integers)
try:
    list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    maximum = find_maximum(list_of_integers)
    print("Максимум в списку:", maximum)
except Exception as e:
    print(e)