"""Topic 3b - Two dimensional arrays.

A 2D array is a list of rows, each row itself a list. Every operation is a
nested loop: the outer loop picks a row, the inner loop walks that row.
"""


def build_grid(rows, cols, fill=0):
    """Build a grid with nested loops.

    Do NOT use [[0] * cols] * rows - that repeats a reference to ONE row, so
    writing to grid[0][0] changes the first column of every row at once.
    """
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(fill)
        grid.append(row)
    return grid


def print_grid(grid):
    for row in grid:
        print(" ".join(str(value).rjust(3) for value in row))


def grid_total(grid):
    running = 0
    for row in grid:
        for value in row:
            running += value
    return running


def grid_average(grid):
    cells = len(grid) * len(grid[0])
    return grid_total(grid) / cells


def grid_largest(grid):
    biggest = grid[0][0]
    for row in grid:
        for value in row:
            if value > biggest:
                biggest = value
    return biggest


def max_of_each_row(grid):
    """Reduce a 2D array to a 1D array - one result per row."""
    maxima = []
    for row in grid:
        biggest = row[0]
        for value in row:
            if value > biggest:
                biggest = value
        maxima.append(biggest)
    return maxima


def count_in_grid(grid, target):
    count = 0
    for row in grid:
        for value in row:
            if value == target:
                count += 1
    return count


def diagonal_totals(grid):
    """Main diagonal is grid[i][i]; the other is grid[i][size - 1 - i]."""
    size = len(grid)
    main = 0
    other = 0
    for i in range(size):
        main += grid[i][i]
        other += grid[i][size - 1 - i]
    return main, other


def move_smallest_to_front(grid):
    """Swap each row's smallest value into that row's first column."""
    for row in grid:
        smallest_index = 0
        for i in range(len(row)):
            if row[i] < row[smallest_index]:
                smallest_index = i
        row[0], row[smallest_index] = row[smallest_index], row[0]
    return grid


if __name__ == "__main__":
    grid = [
        [5, 3, 9],
        [2, 8, 1],
        [7, 4, 6],
    ]

    print("Grid:")
    print_grid(grid)

    print("\nTotal:          ", grid_total(grid))
    print("Average:        ", round(grid_average(grid), 2))
    print("Largest:        ", grid_largest(grid))
    print("Max of each row:", max_of_each_row(grid))
    print("Count of 8:     ", count_in_grid(grid, 8))
    print("Diagonals:      ", diagonal_totals(grid))

    print("\nSmallest moved to front of each row:")
    print_grid(move_smallest_to_front(grid))

    print("\nEmpty 2x4 grid built safely:")
    print_grid(build_grid(2, 4))
