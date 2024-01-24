def find_number(list_of_integers, number):
    index = -1
    for i in range(len(list_of_integers)):
        if list_of_integers[i] == number:
            index = i
            break

    return index
try:
    list_of_integers = [1, 2, 3, 4, 5]
    number = 10
    index = find_number(list_of_integers, number)
    if index == -1:
        print("Число", number, "не знайдено в списку.")
    else:
        print("Число", number, "знаходиться в списку на індексі", index)
except Exception as e:
    print(e)