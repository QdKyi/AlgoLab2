from random import shuffle

from .my_list import MyList
from .my_tuple import MyTuple


def partition(given_array, start, end):
    pivot = given_array[start][0]
    low = start + 1
    high = end

    while True:

        while low <= high and given_array[high][0] > pivot:

            high = high - 1

        while low <= high and not given_array[low][0] > pivot:

            low = low + 1

        if low <= high:
            swap(given_array, low, high)

        else:
            break
    swap(given_array, start, high)

    return high


def quick_sort(given_array, start, end):
    if start >= end:
        return

    my_partition = partition(given_array, start, end)

    quick_sort(given_array, start, my_partition - 1)
    quick_sort(given_array, my_partition + 1, end)


def sort(given_array):

    shuffle(given_array)

    quick_sort(given_array, 0, len(given_array) - 1)


def swap(given_array, first_elem, second_elem):
    given_array[first_elem], given_array[second_elem] = given_array[second_elem], given_array[first_elem]


def calendar_handler(calendar):
    """
    >>> calendar = MyList([MyTuple(MyList([1, 2])), MyTuple(MyList([0, 3])), MyTuple(MyList([2, 4])), MyTuple(MyList([6, 7]))])
    >>> calendar_handler(calendar)
    [(0, 4), (6, 7)]
    """
    sort(calendar)

    final_list = MyList()

    start_time, end_time = calendar[0][0], calendar[0][1]

    for i in range(0, len(calendar)):
        if i < len(calendar) - 1:
            next_elem = calendar[i+1]
        if i >= len(calendar) - 1:
            final_list.append((start_time, calendar[i][1]))
            break
        if end_time >= next_elem[0] and end_time >= next_elem[1]:

            end_time = calendar[i][1]

        elif next_elem[1] >= end_time >= next_elem[0]:

            end_time = next_elem[1]

        else:
            final_list.append((start_time, end_time))
            start_time, end_time = next_elem[0], next_elem[1]

    return final_list


def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()
