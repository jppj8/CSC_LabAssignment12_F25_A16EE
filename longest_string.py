# This program sends a list of strings into function `longest_string()`
# The function returns the index of the longest string in the list.


def longest_string(strings):
    """
    Returns the index of the longest string in the given list of strings.

    @param strings [list]: The list of strings to search.
    @return [int]: The index of the longest string in the given list.
    """

    index_of_longest = 0  # assume the longest string is the first one

    # Loop through the list and update index_of_longest
    for i in range(1, len(strings)):
        if len(strings[i]) > len(strings[index_of_longest]):
            index_of_longest = i

    return index_of_longest


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest_string(strings))  # should print 3
