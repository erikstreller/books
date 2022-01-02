# strong_password_detection.py

import re


def test_password_strength(password: str) -> bool:
    upercaseRegex = re.compile(r"[A-Z]+")
    lowercaseRegex = re.compile(r"[a-z]+")
    digitRegex = re.compile(r"\d+")
    spaceRegex = re.compile(r"\s+")

    if len(password) < 8:
        return False
    if (
        upercaseRegex.search(password)
        and lowercaseRegex.search(password)
        and digitRegex.search(password)
        and not spaceRegex.search(password)
    ):
        return True
    else:
        return False


if __name__ == "__main__":

    password = "a.&Df#-2"

    print(test_password_strength(password))
