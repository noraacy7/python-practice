import ctypes

class Array:

    def __init__(self, size):
        assert size > 0, 'size must be greater than 0'
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)
        self._current = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self._elements[index]
        else:
            raise IndexError('Index out of range!')

    def __setitem__(self, index, value):
        assert 0 <= index < len(self), 'Index out of range!'
        self._elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def print_Array(self):
        value = ''
        for i in range(len(self)):
            value += str(self._elements[i]) + ' '
        print(value)

    def __iter__(self):
        return _ArrayIterator(self._elements)

    '''def __next__(self):
        if self._current < len(self):
            value = self._elements[self._current]
            self._current += 1
            return value
        else:
            raise StopIteration
            '''

class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < len(self._arrayRef):
            value = self._arrayRef[self._current]
            self._current += 1
            return value
        else:
            raise StopIteration

if __name__ == '__main__':
    from collections import Iterable
    a = Array(5)
    print(len(a))
    print(isinstance(a, Iterable))
    a[1] = 5
    a[0] = 'b'
    print(a[1])
    for i in a:
        print(i)
