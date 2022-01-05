#! python3
# mcb.py - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <key> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <key> - Deletes keyword from file.
#        py.exe mcb.pyw delete - Deletes all keywords from file.
#        py.exe mcb.pyw <key> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw help - Lists all available command.

import shelve
import sys
from pathlib import Path

import pyperclip

"""
Open the shelf file in the same location where the script is.
Path(sys.argv[0]).parent is the current script location.
"""
shelfFileLocation = Path(sys.argv[0]).parent / Path("mcb")
mcbShelf = shelve.open(f"{shelfFileLocation}")

"""If opened in command line additional information is shown depending on the input."""
if len(sys.argv) == 3:
    """Save clipboard to keyword or delete keyword"""

    if sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print(f"The current clipboard text is saved under the keyword: {sys.argv[2]}")

    elif sys.argv[1].lower() == "delete":

        if sys.argv[2]:
            del mcbShelf[sys.argv[2]]
            print(
                f"The keyword {sys.argv[2]} with it's corresponding value was deleted."
            )

    else:
        print(
            f"No action for '{sys.argv[1]} {sys.argv[2]}'.\nWrite 'mcb help' for more informations."
        )


elif len(sys.argv) == 2:
    """Copy or delete all keywords. If the keyword excists copy the value to the clipbaord."""

    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(f"All keywords copyed to the clipboard: {str(list(mcbShelf.keys()))}")

    elif sys.argv[1].lower() == "delete":
        for key in list(mcbShelf.keys()):
            del mcbShelf[key]
        print(f"All keywords and values deleted.")

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(f"The text for the keyword: {[sys.argv[1]]} is copyed to the clipboard.")

    elif sys.argv[1].lower() == "help":
        print(
            """
        Available commands are:
        mcb save <keyword> - Saves clipboard to keyword.
        mcb delete <keyword> - Deletes keyword from file.
        mcb <keyword> - Loads keyword to clipboard.
        mcb delete - Deletes all keywords from file.
        mcb list - Loads all keywords to clipboard.
        mcb help - Lists all available command.
        """
        )
else:
    print("Enter 'mcb help' for more information.")

mcbShelf.close()

if __name__ == "__main__":
    pass
