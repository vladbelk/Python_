def calculate_sum_and_average(lst):
    lst = [int(i) for i in lst]
    sum_lst = sum(lst)
    avg_lst = sum_lst / len(lst)
    return sum_lst, avg_lst

try:
    lst = input("Введіть елементи списку через пробіл: ").split()
    sum_lst, avg_lst = calculate_sum_and_average(lst)
    print(f"Сума всіх елементів: {sum_lst}\nСереднє арифметичне: {avg_lst:.2f}")

except Exception as e:
    print(e)