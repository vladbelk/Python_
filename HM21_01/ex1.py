def get_sum_from_list(list, i = 0, sum = 0):
    if i < len(list):
        return get_sum_from_list(list, i + 1, sum + list[i])
    return sum

try:
    if __name__ == "__main__":
        list = [1, 2, 3, 4, 5]
        print(get_sum_from_list(list))
except Exception as e:
    print(e)