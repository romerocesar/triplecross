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

    @staticmethod
    def random_tiles(nrows = 2, ncols = 7):
        return [[random.sample('_dabqezcx', 1)[0] for c in range(ncols)] for r in range(nrows)]

class TripleCross(object):

    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'

    def __init__(self, nrows = 4, ncols = 9):
        self.board = TripleCrossBoard()

    def __str__(self):
        return str(self.board)

    def move(self, op):
        if op not in [UP, RIGHT, LEFT, DOWN]:
            raise Exception('invalid operation: ', op)

if __name__ == '__main__':
    print(TripleCrossBoard(up=False, offset=1))
