def combine_lists(list_1, list_2):
    return list_1 + list_2
try:
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [6, 7, 8, 9, 10]

    combined_list = combine_lists(list_1, list_2)
    print(combined_list)
except Exception as e:
    print(e)