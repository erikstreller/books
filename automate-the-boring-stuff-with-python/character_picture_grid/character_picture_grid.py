# character_picture_grid.py

def print_rotated_grid(grid: list[list[str]]) -> None:

    print("\n".join(map("".join, zip(*grid))))


if __name__ == "__main__":

    grid = [[".", ".", ".", ".", ".", ".", ],
            [".", "X", "X", ".", ".", ".", ],
            ["X", "X", "X", "X", ".", ".", ],
            ["X", "X", "X", "X", "X", ".", ],
            [".", "X", "X", "X", "X", "X", ],
            ["X", "X", "X", "X", "X", ".", ],
            ["X", "X", "X", "X", ".", ".", ],
            [".", "X", "X", ".", ".", ".", ],
            [".", ".", ".", ".", ".", ".", ]]

    print_rotated_grid(grid)
