from utils.my_list import MyList
from utils.my_tuple import MyTuple


def insertion_sort(given_array):
    for i in range(1, len(given_array)):
        if i + 1 >= len(given_array):
            break
        current_position = i

        while current_position > 0 and given_array[i][0] < given_array[i - 1][0]:
            swap(given_array, current_position, current_position - 1)
    return given_array


def swap(given_array, first_elem, second_elem):
    given_array[first_elem], given_array[second_elem] = given_array[second_elem], given_array[first_elem]


def calendar_handler(calendar):
    """
    >>> calendar = MyList([MyTuple(MyList([1, 2])), MyTuple(MyList([0, 3])), MyTuple(MyList([2, 4])), MyTuple(MyList([6, 7]))])
    >>> calendar_handler(calendar)
    [(0, 4), (6, 7)]
    """
    insertion_sort(calendar)

    final_list = MyList()

    start_time, end_time = calendar[0]

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
            start_time, end_time = next_elem

    return final_list


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
