from utils.my_list import MyList
from utils.my_tuple import MyTuple
from utils.sort_and_utils import calendar_handler

if __name__ == '__main__':

    calendar = MyList(
        [MyTuple(MyList([1, 2])), MyTuple(MyList([0, 3])), MyTuple(MyList([2, 4])),
         MyTuple(MyList([6, 7])),MyTuple(MyList([7, 8])), MyTuple(MyList([9, 9]))])
    print(calendar)
    final_list = calendar_handler(calendar)
    print(final_list)

