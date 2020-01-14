"""
Author: Ejona Kocibelli
Project Description: Implementing functions list_copy, list_intersect, list_difference, remove_vowels, check_pwd,
                     and insertion_sort.
"""


def list_copy(l):
    """Function list_copy returns the copy of the list."""
    return [i for i in l]


def list_intersect(l1, l2):
    """Function list_intersect takes two lists as parameters and returns a list with parameters that are in both"""
    return [value for value in l1 if value in l2]


def list_difference(l1, l2):
    """Function list_intersect takes two lists as parameters and returns the values that are in l1 but not in l2"""
    return [value for value in l1 if value not in l2]


def remove_vowels(string):
    """Function remove_vowels returns a copy of string with no vowels in it"""
    # return ''.join([item for item in string.lower() if item not in 'aeoui'])
    return ''.join([item for item in string if item.lower() not in 'aeoui'])


def check_pwd(password):
    """Function check_pwd returns True if password has at least one uppercase, lowercase and ends with a digit,
    otherwise returns False"""
    if any([item.islower() for item in password]) and any([item.isupper() for item in password]) and (password[-1].
                                                                                                      isdigit()):
        return True
    else:
        return False


def insertion_sort(l):
    """Function insertion_sort gets a list and returns a new list that is the sorted version of the list"""
    lst = []
    for item in l:
        for offset, value in enumerate(lst):
            if item < value:
                lst.insert(offset, item)
                break
        else:
            lst.append(item)
    return lst
