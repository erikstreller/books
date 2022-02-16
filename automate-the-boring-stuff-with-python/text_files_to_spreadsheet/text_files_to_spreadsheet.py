# text_files_to_spreadsheet.py

from pathlib import Path

import openpyxl


def txt_to_xlsx():
    directory = Path(__file__).parent.resolve()

    wb = openpyxl.Workbook()
    sheet = wb.active

    files_text = []

    for file in directory.iterdir():
        if file.name.endswith(".txt"):
            f = open(file)
            files_text.append(f.readlines())

    print(files_text)

    column = 1
    for text in files_text:
        row = 1
        for line in text:
            sheet.cell(row=row, column=column, value=line)
            row += 1
        column += 1

    name = "text_to_xlsx.xlsx"
    path = directory / name
    wb.save(str(path))


if __name__ == "__main__":
    txt_to_xlsx()
