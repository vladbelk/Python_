def find_minimum(list_of_integers):

    if list_of_integers:
        minimum = list_of_integers[0]
        for number in list_of_integers:
            if number < minimum:
                minimum = number
        return minimum
    return None

try:
    list_of_integers = [1, 2, 3, 4, 5]

    minimum = find_minimum(list_of_integers)

    print("Мінімальне значення:", minimum)
except Exception as e:
    print(e)
