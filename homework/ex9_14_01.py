def print_line(length, direction, symbol):
    if direction == "горизонтальна":
        for i in range(length):
            print(symbol, end="")
    elif direction == "вертикальна":
        for i in range(length):
            print(symbol)
    else:
        print("Неправильний напрямок лінії.")

try:
    length = int(input("Введіть довжину лінії: "))
    direction = input("Введіть напрямок лінії (горизонтальна/вертикальна): ")
    symbol = input("Введіть символ, з якого складається лінія: ")
    print_line(length, direction, symbol)

except Exception as e:
    print(e)