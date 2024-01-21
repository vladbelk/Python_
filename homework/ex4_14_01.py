def process_text(text):
    sentences = text.split(". ")
    capitalized_text = ". ".join([sentence.capitalize() for sentence in sentences])
    digit_count = sum([capitalized_text.count(str(i)) for i in range(10)])
    punctuation_count = sum([capitalized_text.count(punctuation) for punctuation in [".", ",", ";", ":", "!", "?", "(", ")", "[", "]", "{", "}"]])
    exclamation_count = capitalized_text.count("!")
    return capitalized_text, digit_count, punctuation_count, exclamation_count

try:
    text = input("Введіть текст: ")
    capitalized_text, digit_count, punctuation_count, exclamation_count = process_text(text)
    print(f"Змінений текст: {capitalized_text}\n")
    print(f"Кількість цифр: {digit_count}\n")
    print(f"Кількість розділових знаків: {punctuation_count}\n")
    print(f"Кількість знаків оклику: {exclamation_count}")

except Exception as e:
    print(e)