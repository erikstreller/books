# mad_libs.py

import re


def mad_libs() -> None:
    regex = re.compile(r"(ADJECTIVE|NOUN|VERB)")

    file = open("input.txt")
    text = file.read()
    file.close()

    placeholder: str
    for placeholder in regex.findall(text):
        if placeholder == "ADJECTIVE":
            word = input(f"Enter an {placeholder.lower()}: ")
        else:
            word = input(f"Enter a {placeholder.lower()}: ")

        text = regex.sub(word, text, 1)

    file = open("output.txt", "w")
    file.write(text)
    file.close()


if __name__ == "__main__":
    mad_libs()
