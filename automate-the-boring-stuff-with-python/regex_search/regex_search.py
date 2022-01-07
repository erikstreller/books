# regex_search.py

import re
from pathlib import Path
from typing import Pattern


def print_info() -> None:
    print(
        "Folder not existing. Enter relative or absolute Path ('.' for current location)."
    )


def regex_iterate(path: Path, regex: Pattern[str]) -> None:
    for file in path.iterdir():
        if file.name.endswith(".txt"):
            match = regex.search(open(file).read())
            if match:
                print(f"Found [{match.group()}] in file [{file.name}].")


def evaluate_path(folder: str) -> Path | None:
    if folder.startswith("\\") or folder.startswith("/"):
        folder = folder[:1]
    if folder == ".":
        return Path(__file__).parent.resolve()
    elif (Path(__file__).parent.resolve() / Path(folder)).is_dir():
        return Path(__file__).parent.resolve() / Path(folder)
    else:
        return print_info()


def regex_search() -> None:
    folder = input("Enter folder path: ")
    regex = re.compile(input("Enter search text: "))

    path = evaluate_path(folder)
    if path == None:
        return regex_search()

    regex_iterate(path, regex)


if __name__ == "__main__":
    regex_search()
