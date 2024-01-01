area = 7
mid = area / 2
x = y = 0

n = input('Введіть літеру від а до к:\n')

if n == 'а':
    try:
        for x in range(area):
            for y in range(area):
                if y >= x:
                    print(f' *', end=' ')
                else:
                    print(f'  ', end=' ')
            print()
    except Exception as e:
        print(e)
elif n == 'б':
    try:
        for x in range(area):
            for y in range(area):
                if y <= x:
                    print(f' *', end=' ')
                else:
                    print(f' ', end=' ')
            print()
    except Exception as e:
        print(e)
elif n == 'в':
    try:
        area = 7
        x = y = 0
        while x < area:
            while y < area:
                if x <= area - 1 - y and y >= x:
                    print(f' *', end=' ')
                else:
                    print(f'  ', end=' ')
                y += 1
            x += 1
            y = 0
            print()

    except Exception as e:
        print(e)
elif n == 'г':
    area = 7
    mid = area / 2

    try:
        for x in range(area):
            for y in range(area):
                if y <= x and y >= area - 1 - x:
                    print(f' *', end=' ')
                else:
                    print(f'  ', end=' ')
            print()
    except Exception as e:
        print(e)
elif n == 'д':
    area = 7
    mid = area / 2

    try:
        for x in range(area):
            for y in range(area):
                if y > x - 1 and y < area - x:
                    print(f' *', end=' ')
                elif y + 1 > area - 1 - x and y - 1 < x:
                    print(f' *', end=' ')
                else:
                    print(f'  ', end=' ')
            print()
    except Exception as e:
        print(e)
elif n == 'е':
    area = 7
    mid = area / 2

    try:
        for x in range(area):
            for y in range(area):
                if y <= x and y <= area - 1 - x:
                    print(f' *', end=' ')
                elif x >= area - 1 - y and y >= x:
                    print(f' *', end=' ')
                else:
                    print(f'  ', end=' ')
            print()
    except Exception as e:
        print(e)
elif n == 'ж':
    area = 7
    mid = area / 2

    try:
        for x in range(area):
            for y in range(area):
                if y <= x and y <= area - 1 - x:
                    print(f' *', end=' ')
                else:
                    print(f' ', end=' ')
            print()
    except Exception as e:
        print(e)
elif n == 'з':
    try:
        area = 7
        x = y = 0
        while x < area:
            while y < area:
                if x >= area - 1 - y and y >= x:
                    print(f' *', end=' ')
                else:
                    print(f'  ', end=' ')
                y += 1
            x += 1
            y = 0
            print()

    except Exception as e:
        print(e)
elif n == 'и':
    try:
        area = 7
        x = y = 0
        while x < area:
            while y < area:
                if x <= area - 1 - y:
                    print(f' *', end=' ')
                else:
                    print(f'  ', end=' ')
                y += 1
            x += 1
            y = 0
            print()

    except Exception as e:
        print(e)
elif n == 'к':
    try:
        area = 7
        x = y = 0
        while x < area:
            while y < area:
                if x >= area - 1 - y:
                    print(f' *', end=' ')
                else:
                    print(f'  ', end=' ')
                y += 1
            x += 1
            y = 0
            print()
    except Exception as e:
        print(e)
else:
    print("Будь ласка введіть літеру від 'а' до 'к'")
