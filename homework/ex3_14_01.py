def count_sentences(text):
    sentences = text.split(".")
    sentences = [sentence for sentence in sentences if sentence]

    return len(sentences)

try:

    text = input("Введіть текст: ")
    sentences_count = count_sentences(text)
    print("Кількість речень в тексті:", sentences_count)


except Exception as e:
    print(e)