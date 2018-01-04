from my_array import Array


class Array2D:
    def __init__(self, nrows, ncols):
        self._array1 = Array(nrows)
        for i in range(nrows):
            self._array1[i] = Array(ncols)
            self._array1[i].clear(None)

    def numRows(self):
        return len(self._array1)

    def numCols(self):
        return len(self._array1[0])

    def clear(self, value):
        for i in range(len(self._array1)):
            self._array1[i].clear(value)

    def __getitem__(self, indexTuple):
        assert len(indexTuple) == 2, 'Invalid number of array subscripts'
        row = indexTuple[0]
        col = indexTuple[1]
        assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), 'Index out of range'
        return self._array1[row][col]

    def __setitem__(self, indexTuple, value):
        assert len(indexTuple) == 2, 'Invalid number of array subscripts'
        row = indexTuple[0]
        col = indexTuple[1]
        assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), 'Index out of range'
        self._array1[row][col] = value

    def print_Array2D(self):
        for i in self._array1:
            i.print_Array()