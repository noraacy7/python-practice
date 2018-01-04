from life import LifeGrid


INIT_CONFIG = [ (1,2), (2,1), (2,2), (2,3) ]

# Set the size of the grid.
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of generations.
NUM_GENS = 8

def main():
    grid = LifeGrid( GRID_WIDTH, GRID_HEIGHT )
    grid.configure( INIT_CONFIG )
    grid.drawGrid()
    print('\n')
    for i in range(NUM_GENS):
        evolve(grid)
        grid.drawGrid()
        print('\n')

# Generates the next generation of organisms.
def evolve( grid ):
# List for storing the live cells of the next generation.
    liveCells = list()
# Iterate over the elements of the grid.
    for i in range( grid.numRows() ) :
        for j in range( grid.numCols() ) :
# Determine the number of live neighbors for this cell.
            neighbors = grid.numLiveNeighbors( i, j )

# Add the (i,j) tuple to liveCells if this cell contains
# a live organism in the next generation.
            if (neighbors == 2 and grid.isLiveCell( i, j )) or \
                (neighbors == 3 ) :
                liveCells.append( (i, j) )

# Reconfigure the grid using the liveCells coord list.
    grid.configure( liveCells )


if __name__ == '__main__':
    main()