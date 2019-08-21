from enum import Enum
class Colour(Enum):
    white = 1
    black = -1

class Piece:
    """
        Abstract class that outlines the common methods and fields
        for all chess pieces (Rook, Knight, Bishop, Queen, King, Pawn)
    """

    def __init__(self, position, colour):
        self.pos = self.x, self.y = position
        self.colour = colour

    # returns a list of (x,y) such that the piece could move to those squares
    def getCanidiateSquares(self, board):
        raise NotImplementedError

    # coords = index of square to move to
    def  move(self, coords):
        self.pos = coords
        self.x = coords.x
        self.y = coords.y

class Pawn(Piece):
    def getCanidiateSquares(self, board):
        direction = self.colour
        candidates = [(self.x, self.y + direction)]
        diagonals = [(self.x + 1, self.y + direction), (self.x - 1, self.y + direction)]
        for x,y in diagonals:
            piece = board[y][x]
            if(piece != None and piece.colour == -1*piece.colour):
                candidates.append((x,y))

class Rook(Piece):
    def getCanidiateSquares(self, board):
        direction = self.colour
        candidates = [(self.x, self.y + direction)]
        diagonals = [(self.x + 1, self.y + direction), (self.x - 1, self.y + direction)]
        for x,y in diagonals:
            piece = board[y][x]
            if(piece != None and piece.colour == -1*piece.colour):
                candidates.append((x,y))

class Knight(Piece):
    def getCanidiateSquares(self, board):
        direction = 1 if (self.colour == Colour.white) else -1
        candidates = [(self.x, self.y + direction)]
        diagonals = [(self.x + 1, self.y + direction), (self.x - 1, self.y + direction)]
        for x,y in diagonals:
            piece = board[y][x]
            if(piece != None and piece.colour == -1*piece.colour):
                candidates.append((x,y))

class Bishop(Piece):
    def getCanidiateSquares(self, board):
        direction = 1 if (self.colour == Colour.white) else -1
        candidates = [(self.x, self.y + direction)]
        diagonals = [(self.x + 1, self.y + direction), (self.x - 1, self.y + direction)]
        for x,y in diagonals:
            piece = board[y][x]
            if(piece != None and piece.colour == -1*piece.colour):
                candidates.append((x,y))

class Queen(Piece):
    def getCanidiateSquares(self, board):
        direction = 1 if (self.colour == Colour.white) else -1
        candidates = [(self.x, self.y + direction)]
        diagonals = [(self.x + 1, self.y + direction), (self.x - 1, self.y + direction)]
        for x,y in diagonals:
            piece = board[y][x]
            if(piece != None and piece.colour == -1*piece.colour):
                candidates.append((x,y))

class King(Piece):
    def getCanidiateSquares(self, board):
        direction = 1 if (self.colour == Colour.white) else -1
        candidates = [(self.x, self.y + direction)]
        diagonals = [(self.x + 1, self.y + direction), (self.x - 1, self.y + direction)]
        for x,y in diagonals:
            piece = board[y][x]
            if(piece != None and piece.colour == -1*piece.colour):
                candidates.append((x,y))