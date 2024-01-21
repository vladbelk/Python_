def count_occurrences(lst, num):
    count = lst.count(num)
    return count

try:
    lst = input("Введіть елементи списку через пробіл: ").split()
    num = input("Введіть число: ")
    count = count_occurrences(lst, num)
    print(f"Число {num} зустрічається у списку {count} разів.")

except Exception as e:
    print(e)