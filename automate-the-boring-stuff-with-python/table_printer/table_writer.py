# table_writer.py

def printTable(table: list) -> None:
    columnWidth = [0] * len(table)

    for i, innerTable in enumerate(table):
        columnWidth[i] = len(max(innerTable, key=len))

    zippedTable = list(zip(*table))
    newTable = []

    for row in zippedTable:
        newRow = []
        for cell in row:
            cell: str
            newRow.append(cell.rjust(columnWidth[row.index(cell)], "."))

        newTable.append(newRow)

    newTable = "\n".join(map(" ".join, newTable))

    print(newTable)


if __name__ == "__main__":

    stuff = [
        ["apples", "oranges", "cherries", "banana"],
        ["Alice", "Bob", "Carol", "David"],
        ["dogs", "cats", "moose", "goose"]
    ]

    printTable(stuff)
