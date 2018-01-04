from  array2D import Array2D


class LifeGrid:
    LIVE = 1
    DEAD = 0

    def __init__(self, nrows, ncols):
        assert nrows > 0 and ncols > 0, 'number of rows or cols must be greater than 0!'
        self._grid = Array2D(nrows, ncols)
        self.configure(list())

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def configure(self, coordlist):
        self._grid.clear(LifeGrid.DEAD)
        for coord in coordlist:
            self.setCell(coord[0], coord[1])

    def clearCell(self, row, col):
        assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), 'index out of range'
        self._grid[row, col] = LifeGrid.DEAD

    def setCell(self, row, col):
        assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), 'index out of range'
        self._grid[row, col] = LifeGrid.LIVE

    def isLiveCell(self, row, col):
        assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), 'index out of range'
        return self._grid[row, col] == LifeGrid.LIVE

    def numLiveNeighbors(self, row, col):
        num = 0
        assert 0 <= row < self.numRows() and 0 <= col < self.numCols(), 'index out of range'
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < self.numRows() and 0 <= j < self.numCols():
                    if self.isLiveCell(i, j):
                        if i == row and j == col:
                            num = num
                        else:
                            num += 1
        return num

    def drawGrid(self):
        self._grid.print_Array2D()


g = LifeGrid(5, 6)
g.setCell(4,4)
g.setCell(4,5)
g.setCell(0,0)
g.setCell(1,0)
g.drawGrid()
print(g.numLiveNeighbors(2,0))
