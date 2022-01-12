# find_unneeded_files.py

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


def find_unneeded_files(folder: str, size: int) -> None:

    path = evaluate_path(folder)
    if path == None:
        return

    for file in path.rglob("*"):
        file_size = file.stat().st_size
        if file_size > size:
            print(f"Deleted file {file.name} with size {file_size} bytes.")


if __name__ == "__main__":
    find_unneeded_files(".", 1000)
