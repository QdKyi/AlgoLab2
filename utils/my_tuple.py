
class MyTuple():

    def __init__(self, data=None):
        super(MyTuple, self).__init__()
        if data is not None:
            self._tuple = tuple(data)
        else:
            self._tuple = tuple()

    def __repr__(self):
        return str(self._tuple)

    def __getitem__(self, ii):
        return self._tuple[ii]

    def __str__(self):
        return str(self._tuple)
