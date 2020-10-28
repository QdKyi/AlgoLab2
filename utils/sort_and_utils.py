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

    for i in range(calendar.__len__()):
        if i >= calendar.__len__():
            break
        start_time = calendar[i][0]
        end_time = calendar[i][1]
        for j in range(i + 1, calendar.__len__()):
            if end_time >= calendar[i + 1][0] and end_time >= calendar[i + 1][1]:

                end_time = calendar[i][1]

                calendar.remove(calendar[i + 1])
            elif calendar[i + 1][1] >= end_time >= calendar[i + 1][0]:

                end_time = calendar[i + 1][1]

                calendar.remove(calendar[i + 1])

        final_list.append((start_time, end_time))

    return final_list


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)