# selective_copy.py

import shutil
from pathlib import Path


def print_info() -> None:
    print(
        "Folder not existing. Enter relative or absolute Path ('.' for current location)."
    )


def evaluate_path(folder: str) -> Path | None:
    if folder.startswith("\\") or folder.startswith("/"):
        folder = folder[:1]
    if folder == ".":
        return Path(__file__).parent.resolve()
    elif (Path(__file__).parent.resolve() / Path(folder)).is_dir():
        return Path(__file__).parent.resolve() / Path(folder)
    else:
        return print_info()


def selective_copy() -> None:
    folder = input("Enter folder path: ")
    file_extension = input("Enter file extension: ")

    path = evaluate_path(folder)
    if path == None:
        return selective_copy()

    destination = path / f"copy_of_{file_extension[1:]}"

    # create destination folder if it does not exist
    if not destination.exists():
        Path.mkdir(destination)

    # search for all files with the suffix {file_extension}
    # copy them into the destination folder
    for file in path.rglob(f"*{file_extension}"):
        if file != destination / file.name:
            shutil.copy(file, destination)
            print(f"{file.name} copied to {destination}")

    # if no files are copied, delete destination folder
    empty = next(destination.iterdir(), None)
    if empty == None:
        shutil.rmtree(destination)
        print(f"No files found with the suffix: {file_extension}")


if __name__ == "__main__":
    selective_copy()
