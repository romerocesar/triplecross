import logging
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class TripleCrossBoard(object):

    def __init__(self, nrows = 2, ncols = 7, offset = 0, up = True):
        self.offset = offset
        self.max_offset = 2
        self.pad = 3
        self.up = up
        self.tiles = TripleCrossBoard.random_tiles(nrows = nrows, ncols = ncols)
        self.extras = ['_']*4

    def __str__(self):
        row = []
        ans = ''
        # top row first
        if self.up:
            row = [' ' for x in range(self.max_offset)] + self.extras[:2]
        else:
            row = [' ' for x in range(self.max_offset + self.pad)] + self.extras[2:]
        ans = ''.join(row) + '\n'
        # center tiles
        for row in self.tiles:
            pad = [' ' for x in range(self.offset)]
            ans += ''.join(pad + row) + '\n'
        # bottom rows
        if self.up:
            row = [' ' for x in range(self.max_offset + self.pad)] + self.extras[2:]
        else:
            row = [' ' for x in range(self.max_offset)] + self.extras[2:]
        ans += ''.join(row) + '\n'

        return ans

    def __getitem__(self, key):
        return self.tiles[key]

    @staticmethod
    def random_tiles(nrows = 2, ncols = 7):
        ans = [['_' for c in range(ncols)] for r in range(nrows)]
        pop = list(range(nrows*ncols))
        tiles = random.sample(pop, 9)
        symbols = 'dddabqezc'
        for tile, symbol in zip(tiles, symbols):
            row = tile // ncols
            col = tile % ncols
            ans[row][col] = symbol
        return ans

class TripleCross(object):

    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
    DOME_UL = 'q'
    DOME_UR = 'e'
    DOME_LL = 'z'
    DOME_LR = 'c'

    def __init__(self, nrows = 4, ncols = 9):
        self.nrows = nrows
        self.ncols = ncols
        self.board = TripleCrossBoard()

    def __str__(self):
        return str(self.board)

    def goal(self):
        '''Returns True when the current state corresponds to one of the valid
        goals defined for the TripleCross game.
        '''
        return self._dome() or self._dots() or self._binarts()

    def move(self, op):
        if op not in [UP, RIGHT, LEFT, DOWN]:
            raise Exception('invalid operation: ', op)

    def _dome(self):
        row,col = index(DOME_UL)
        return row != 0 and col != self.ncols - 1 \
        and self.board[row][col+1] == DOME_UR \
        and self.board[row+1][col+1] == DOME_LR \
        and self.board[row+1][col-1] == DOME_LL

    def _dots(self):
        return false

    def _binarts(self):
        return false

if __name__ == '__main__':
    print(TripleCrossBoard(up=False, offset=1))
