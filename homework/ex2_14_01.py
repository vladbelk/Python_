def find_and_replace_reserved_words(text, reserved_words):
    for word in reserved_words:
        text = text.replace(word, word.upper())

    assert isinstance(text, object)
    return text

try:
    text = input("Введіть текст: ")
    reserved_words = input("Введіть список зарезервованих слів через кому: ").split(",")
    changed_text = find_and_replace_reserved_words(text, reserved_words)
    print("Змінений текст:")
    print(changed_text)


except Exception as e:
    print(e)