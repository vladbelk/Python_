def count_elements(list_of_integers):
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for integer in list_of_integers:
        if integer % 2 == 0:
            even_count += 1
        elif integer % 2 == 1:
            odd_count += 1
        if integer >= 0:
            positive_count += 1
        else:
            negative_count += 1

    return even_count, odd_count, positive_count, negative_count
try:
    list_of_integers = [1, 2, 3, 4, 5]
    count_of_elements = count_elements(list_of_integers)

    print("Кількість парних елементів:", count_of_elements[0])
    print("Кількість непарних елементів:", count_of_elements[1])
    print("Кількість додатних елементів:", count_of_elements[2])
    print("Кількість від'ємних елементів:", count_of_elements[3])
except Exception as e:
    print(e)