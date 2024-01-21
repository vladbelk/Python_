from colorama import init, Fore, Style

def display_text():
    init()
try:

    quote = "\"Don't let the noise of others' opinions \ndrown out your own inner voice.\""
    author = "Steve Jobs"
    print(f'{Fore.WHITE}{quote}\n{Fore.YELLOW}{author}{Style.RESET_ALL}')

    display_text()

except Exception as e:
    print(e)