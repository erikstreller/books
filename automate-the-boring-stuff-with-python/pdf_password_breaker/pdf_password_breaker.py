# pdf_password_breaker.py

from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter


def brute_force_password_atk(dictionary_path: Path, encrypted_path: Path) -> None:

    dictionary_file = open(str(dictionary_path))
    encrypted_file = PdfFileReader(str(encrypted_path), "rb")

    password = ""
    trys = 0
    for word in dictionary_file:
        word = word.replace("\n", "")
        trys += 1
        print(trys, end="\r")
        if encrypted_file.decrypt(word.upper()) == 1:
            password = word.upper()
            break
        elif encrypted_file.decrypt(word.lower()) == 1:
            password = word.lower()
            break

    print(f"Password: {password}")
    print(f"Trys: {trys}")


if __name__ == "__main__":
    path = Path(__file__).parent.resolve()

    dictionary_path = path / "dictionary.txt"
    encrypted_path = path / "encrypted.pdf"

    brute_force_password_atk(dictionary_path, encrypted_path)
