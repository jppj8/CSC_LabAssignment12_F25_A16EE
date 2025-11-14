# This program sends a matrix to the function `count_matching()`, and the
# function returns the number of matched elements in the matrix.


def count_matching(matrix, target):
    """
    Counts how many elements in the 2-dimensional nested list (matrix) match
    the given target value.

    @param matrix [list]: list of list of integers
    @param target [int]: the value to match
    @return [int]: the number of matching elements
    """

    # set initial variable `count`
    count = 0

    # external loop to get all nested lists (rows)
    for row in matrix:
        # inner loop to get every element in the row
        for value in row:
            if value == target:
                count += 1

    return count


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 1, 0]]
    print(count_matching(m, 1))  # should print 4
