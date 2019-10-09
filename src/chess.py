import numpy as np
import pieces
from pieces import Colour, Piece, Pawn, Rook, Knight, Bishop, Queen, King


class Chess:
    """
        Models the systems of logic involved in a chess game
        Need to initialise board with pieces
    """

    def __init__(self):
        self.turnColour = Colour.white
        self.board = []
        self.isOver = False

    def on_init(self):
        pawnRow = lambda y, c: [Pawn((x, y), c) for x in range(8)]
        constructPieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        pieceRow = lambda y, c: [constructPieces[x]((x, y), c) for x in range(8)]
        emptyRow = [None, None, None, None, None, None, None, None]
        for y in range(8):
            row = emptyRow.copy()
            if y == 0:
                row = pieceRow(y, Colour.black)
            elif y == 7:
                row = pieceRow(y, Colour.white)
            elif y == 1:
                row = pawnRow(y, Colour.black)
            elif y == 6:
                row = pawnRow(y, Colour.white)
            self.board.append(row)

    def move(self, fromPos, toPos):
        (fromX, fromY) = fromPos
        (toX, toY) = toPos
        fromPiece = self.board[fromY][fromX]
        if fromPiece is None or fromPiece.colour != self.turnColour:
            return False
        candidates = fromPiece.getCanidiateSquares()
        toPiece = self.board[toY][toX]
        print(toPos)
        print(fromPiece.getPath(fromPos, toPos))
        print(toPiece == None)
        print(toPos in fromPiece.getPath(fromPos, toPos))
        moveIsNotBlocked = all(self.board[y][x] == None for (x,y) in fromPiece.getPath(fromPos, toPos))
        isLegal = (toPos in candidates) and moveIsNotBlocked and ((toPiece is None) or toPiece.colour != fromPiece.colour)
        if isLegal:
            self.board[fromY][fromX] = None
            self.board[toY][toX] = fromPiece
            fromPiece.move(toPos)
            # Invert turn colour
            self.turnColour *= -1 
        return isLegal
