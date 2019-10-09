from enum import IntEnum
from itertools import cycle, islice, dropwhile, chain, product


class Colour(IntEnum):
    white = -1
    black = 1


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

    def getPath(self, fromCo, toCo):
        raise NotImplementedError

    def onBoard(self, candidates):
        return list(
            filter(lambda xy: xy[0] >= 0 and xy[1] >= 0 and xy[0] <= 7 and xy[1] <= 7, candidates)
        )

    # coords = index of square to move to
    def move(self, coords):
        self.position = coords
        self.x = coords[0]
        self.y = coords[1]


class Pawn(Piece):
    def __init__(self, position, colour):
        super().__init__(position, colour)
        self.hasMoved = False
    
    def getCanidiateSquares(self):
        direction = self.colour
        forward = [(self.x, self.y + direction)]
        firstMove = [(self.x, self.y + 2*direction)]
        diagonals = [(self.x + 1, self.y + direction), (self.x - 1, self.y + direction)]
        candidates = forward + diagonals
        if not self.hasMoved: 
            candidates += firstMove
        return self.onBoard(candidates)

    def getPath(self, fromCo, toCo):
        direction = self.colour
        path = []
        if fromCo[0] == toCo[0]:
            path += [(fromCo[0], fromCo[1] + direction)]
        if toCo[1] == fromCo[1] + 2:
            path += [(fromCo[0], fromCo[1] + 2*direction)]
        return path 

    def move(self, coords):
        super().move(coords)
        self.hasMoved = True

p = Pawn((3, 3), Colour.white)
print(p.getCanidiateSquares())


class Rook(Piece):
    def getCanidiateSquares(self):
        horizontal = [(self.x, y) for y in range(1, 8)]
        vertical = [(x, self.y) for x in range(1, 8)]
        candidates = horizontal + vertical
        return self.onBoard(candidates)
    
    def getPath(self, fromCo, toCo):
        (fromX, fromY) = fromCo
        (toX, toY) = toCo
        assert fromX == toX or fromY == toY 
        path = []
        if fromX == toX:
            if toY > fromY:
                path = [(fromX, fromY + i) for i in range(1, toY - fromY)]
            else: 
                path = [(fromX, fromY - i) for i in range(1, toY - fromY)]
        else:
            if toX > fromX:
                path = [(fromX + i, fromY) for i in range(1, toX - fromX)]
            else: 
                path = [(fromX - i, fromY) for i in range(1, toX - fromX)]

        return path

class Knight(Piece):
    def getCanidiateSquares(self):
        moves = product([1, -1], [2, -2])
        candidates = list(
            chain.from_iterable(
                [[(self.x + x, self.y + y), (self.x + y, self.y + x)] for (x, y) in moves]
            )
        )
        return self.onBoard(candidates)
    
    def getPath(self, fromCo, toCo):
        return []

class Bishop(Piece):
    def getCanidiateSquares(self):
        delta = [1, -1]
        diagonals = [
            (self.x + scale * x, self.y + scale * y)
            for (x, y) in product(delta, repeat=2)
            for scale in range(1, 8)
        ]
        candidates = diagonals
        return self.onBoard(candidates)

    def getPath(self, fromCo, toCo):
        (fromX, fromY) = fromCo
        (toX, toY) = toCo
        assert abs(fromX - toX) == abs(fromY - toY) 
        path = []
        pathLength = abs(fromX - toX)
        if toX > fromX:
            if toY > fromY:
                path = [(fromX + i, fromY + i) for i in range(1, pathLength)]
            else: 
                path = [(fromX + i, fromY - i) for i in range(1, pathLength)]
        else:
            if toY > fromY:
                path = [(fromX - i, fromY + i) for i in range(1, pathLength)]
            else: 
                path = [(fromX - i, fromY - i) for i in range(1, pathLength)]

        return path

class Queen(Piece):
    def getCanidiateSquares(self):
        tempBishopCandidates = Bishop(self.position, self.colour).getCanidiateSquares()
        tempRookCandidates = Rook(self.position, self.colour).getCanidiateSquares()
        candidates = tempBishopCandidates + tempRookCandidates
        return self.onBoard(candidates)
    
    def getPath(self, fromCo, toCo):
        bishop = Bishop(self.position, self.colour)
        rook = Rook(self.position, self.colour)
        if fromCo[0] == toCo[0] or fromCo[1] == toCo[1]:
            return rook.getPath(fromCo, toCo) 
        else:
            return bishop.getPath(fromCo, toCo)

class King(Piece):
    def __init__(self, position, colour):
        super().__init__(position, colour)
        self.inCheck = False

    def getCanidiateSquares(self):
        delta = [-1, 0, 1]
        candidates = [(self.x + x, self.y + y) for (x, y) in product(delta, repeat=2)]
        candidates.remove(self.position)
        return self.onBoard(candidates)
    
    def getPath(self, fromCo, toCo):
        return []
    
    def putInCheck(self):
        self.inCheck = True

    def outOfCheck(self):
        self.inCheck = False
