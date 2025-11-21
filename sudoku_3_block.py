def block_check(sudoku, row_no, column_no):
    """
    Checks if a 3x3 block in a Sudoku grid is valid.
    A block is valid if numbers 1–9 appear at most once (0s are ignored).

    @param sudoku: list of list of int - The Sudoku grid.
    @param row_no: int - The starting row index of the block.
    @param column_no: int - The starting column index of the block.

    @return: bool - True if the block is correct, False otherwise.
    """

    checked = set()  # record numbers we've already seen in this block

    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            num = sudoku[i][j]

            if num != 0:             # ignore empty spots
                if num in checked:   # duplicate found
                    return False
                checked.add(num)     # remember this number

    return True  # no duplicates found
