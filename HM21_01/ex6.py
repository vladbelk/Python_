def calculate_powers(degree, list_of_integers):
    list_of_powers = []
    for integer in list_of_integers:
        power = integer ** degree
        list_of_powers.append(power)
    return list_of_powers
try:
    list_of_integers = [1, 2, 3, 4, 5]
    list_of_powers = calculate_powers(3, list_of_integers)
    print(list_of_powers)
except Exception as e:
    print(e)