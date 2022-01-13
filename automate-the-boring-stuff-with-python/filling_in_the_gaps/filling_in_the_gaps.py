# filling_in_the_gaps.py

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


def find_gaps(folder: str, prefix: str) -> None:
    """Find gaps in numbered files with a given prefix and rename them numbered consecutively."""

    # evaluate if folder exists and if path is absolute or relative
    path = evaluate_path(folder)
    if path == None:
        return

    # search for files with the given prefix and write the paths into a list
    files: list[Path] = []
    extension: list[str] = []
    for file in path.iterdir():
        if not file.is_file():
            continue
        if not file.name.startswith(prefix):
            continue

        files.append(file)
        extension.append(file.suffix)

    # create consecutively numbered files and delete the old ones
    for i in range(len(files)):
        new_name = f"{prefix}" + "{:0>3}".format(i + 1) + f"{extension[i]}"

        # no need to rename file if it has the right number
        if files[i].name == new_name:
            continue

        destination_path = (path / new_name).absolute()
        shutil.copy(files[i], destination_path)
        files[i].unlink()

        print(f"renamed {files[i].name} to {new_name}")


if __name__ == "__main__":
    find_gaps(".", "spam")
