def column_check(sudoku, column_no):
    """
    Checks if a given column in a Sudoku grid is valid.
    A column is valid if numbers 1 to 9 appear at most once (0s are ignored).

    @param sudoku [list]: list of list of int, the Sudoku grid
    @param column_no [list]: the index of the column to check (0 based)

    @return [bool], returns True if the column is correct, False otherwise.
    """

    checked = set()  # record numbers we've already seen in this column

    for row in sudoku:
        num = row[column_no]     # get the number at this column in the current row

        if num != 0:             # ignore empty spots
            if num in checked:   # duplicate found
                return False
            checked.add(num)     # remember this number

    return True  # no duplicates found


if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    print(column_check(sudoku, 0))  # False (two 2s)
    print(column_check(sudoku, 1))  # True (no duplicates)
