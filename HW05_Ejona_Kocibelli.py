"""
Author: Ejona Kocibelli
Project Description: Implementing functions reverse, reverse_enumerate, find_second and get_lines.
"""


def reverse(string):
    """Function reverse gets a string and returns the reversed version of that string."""
    reversed_string = ""
    index = len(string)
    while index:
        index -= 1
        reversed_string += string[index]
    return reversed_string


def rev_enumerate(seq):
    """Function reverse_enumerate gets a sequence and yields the reversed offset and sequence."""
    for offset in range(len(seq)-1, -1, -1):
        yield offset, seq[offset]


def find_second(target, string):
    """Function second_occurrence gets a substring and string and returns the second occurrence of the substring on that
     string."""
    second_occurrence = string.find(target, string.find(target) + 1)
    return second_occurrence


def get_lines(file_path):
    """Function get lines gets opens a file, if the file is not found returns a FileNotFoundError, otherwise
    opens the file and reads line by line, if the lines end with '\' concatenates those lines, if the line has
    a comment in it checks the '#' position. If '#' in the beginning of line, ignores the line and continues to
    next one, if '#' in different positions, yield the line up to but not including '#'. If line is no comment, yields
    the line"""
    try:
        fp = open(file_path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't open {file_path}")
    else:
        with fp:
            for line in fp:
                line = line.rstrip('\n')
                while line.endswith('\\'):
                    line = line[:-1] + fp.readline().rstrip('\n')

                offset = line.find('#')
                if offset == -1:
                    yield line
                elif offset == 0:
                    continue
                else:
                    yield line[:offset]