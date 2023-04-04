import random

def create_sudoku_grid():
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(random.randint(1, 9))
        grid.append(row)
    return grid

def print_sudoku_grid(grid):
    for i, row in enumerate(grid):
        if i % 3 == 0 and i > 0:
            print("-" * 21)
        for j, cell in enumerate(row):
            if j % 3 == 0 and j > 0:
                print("|", end=" ")
            print(cell, end=" ")
        print()

def main():
    grid = create_sudoku_grid()
    print_sudoku_grid(grid)

if __name__ == "__main__":
    main()
