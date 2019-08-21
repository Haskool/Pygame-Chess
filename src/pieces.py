from enum import IntEnum
from itertools import cycle, islice, dropwhile, chain, product


class Colour(IntEnum):
    white = 1
    black = -1


class Piece:
    """
        Abstract class that outlines the common methods and fields
        for all chess pieces (Rook, Knight, Bishop, Queen, King, Pawn)
    """

    def __init__(self, position, colour):
        self.position = self.x, self.y = position
        self.colour = colour

    # returns a list of (x,y) such that the piece could move to those squares
    def getCanidiateSquares(self):
        raise NotImplementedError

    def onBoard(self, candidates):
        return list(
            filter(lambda xy: xy[0] >= 0 and xy[1] >= 0 and xy[0] <= 7 and xy[1] <= 7, candidates)
        )

    # coords = index of square to move to
    def move(self, coords):
        self.pos = coords
        self.x = coords.x
        self.y = coords.y


class Pawn(Piece):
    def getCanidiateSquares(self):
        direction = self.colour
        forward = [(self.x, self.y + direction)]
        diagonals = [(self.x + 1, self.y + direction), (self.x - 1, self.y + direction)]
        candidates = forward + diagonals
        return self.onBoard(candidates)


p = Pawn((0, 0), Colour.white)
print(p.getCanidiateSquares())


class Rook(Piece):
    def getCanidiateSquares(self):
        horizontal = [(self.x, y) for y in range(1, 8)]
        vertical = [(x, self.y) for x in range(1, 8)]
        candidates = horizontal + vertical
        return self.onBoard(candidates)


r = Rook((3, 2), Colour.white)
print(r.getCanidiateSquares())


class Knight(Piece):
    def getCanidiateSquares(self):
        createL = lambda xs, ys: [(self.x + x, self.y + y) for x in xs for y in ys]
        moves = cycle([[1, -1], [2]])
        xss = list(islice(moves, 4))
        yss = list(islice(moves, 1, 5))
        candidates = list(chain.from_iterable([createL(xs, ys) for (xs, ys) in zip(xss, yss)]))
        return self.onBoard(candidates)


k = Knight((3, 2), Colour.white)
print(k.getCanidiateSquares())
print(k.getCanidiateSquares()[0:4])


class Bishop(Piece):
    def getCanidiateSquares(self):
        diagonals = [[(self.x + i, self.y + i), (self.x - i, self.y + i)] for i in range(1, 8)]
        candidates = list(chain.from_iterable(diagonals))
        return self.onBoard(candidates)


b = Bishop((0, 0), Colour.white)
print(b.getCanidiateSquares())


class Queen(Piece):
    def getCanidiateSquares(self):
        tempBishopCandidates = Bishop(self.position, self.colour).getCanidiateSquares()
        tempRookCandidates = Rook(self.position, self.colour).getCanidiateSquares()
        candidates = tempBishopCandidates + tempRookCandidates
        return self.onBoard(candidates)


q = Queen((4, 4), Colour.white)
print(q.getCanidiateSquares())


class King(Piece):
    def getCanidiateSquares(self):
        delta = [-1, 0, 1]
        candidates = [(self.x + x, self.y + y) for (x, y) in product(delta, repeat=2)]
        candidates.remove(self.position)
        return self.onBoard(candidates)


king = King((3, 3), Colour.white)
print(king.getCanidiateSquares())
