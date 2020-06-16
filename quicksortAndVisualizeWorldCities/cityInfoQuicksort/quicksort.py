# Sunint Bindra
# February 22, 2019
# quicksort.py
# lab3cs1
# This program has functions that sorts a list of integers or strings in a given order.


# This compares two values and returns True or False depending on which value is greater
def compare_func(a, b):
    if type(a) == int:
        if b <= a:
            return True
        else:
            return False
    if type(a) == str:
        if b.lower() <= a.lower():
            return True
        else:
            return False


# This function essentially splits the given list down the middle using the vital pivot value as information
def partition(the_list, p, r, compare_func):

    pivot = the_list[r]
    i = p - 1
    j = p
    while j < r:
        if compare_func(the_list[j], pivot):
            j += 1
        else:
            i += 1
            (the_list[i], the_list[j]) = (the_list[j], the_list[i])
            j += 1
    if j == r:
        (the_list[r], the_list[i+1]) = (the_list[i+1], the_list[r])
    return i + 1


# This continues the partition process and sorts the split up lists according to the preferences set
def quicksort(the_list, p, r, compare_func):
    if p < r:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, q + 1, r, compare_func)
        quicksort(the_list, p, q - 1, compare_func)


# This calls the quicksort function to sort
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)
