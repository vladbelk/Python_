def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    return text == text[::-1]


try:
    text = input("Введіть рядок: ")
    if is_palindrome(text):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")


except Exception as e:
    print(e)
