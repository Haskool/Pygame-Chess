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
        emptyRow = [None] * 8
        for y in range(8):
            row = emptyRow
            if y == 0:
                row = pieceRow(y, Colour.white)
            elif y == 7:
                row = pieceRow(y, Colour.black)
            elif y == 1:
                row = pawnRow(y, Colour.white)
            elif y == 6:
                row = pawnRow(y, Colour.black)
            self.board.append(row)

    def move(self, fromPos, toPos):
        print("moving: " + str(fromPos) + "to " + str(toPos))
        fromPiece = self.board[fromPos[1]][fromPos[0]]
        if fromPiece is None or fromPiece.colour != self.turnColour:
            return None
        candidates = fromPiece.getCanidiateSquares()

        toPiece = self.board[toPos[1]][toPos[0]]
        if toPos in candidates and ((toPiece is None) or toPiece.colour != fromPiece.colour):
            self.board[fromPos[1]][fromPos[0]] = None
            self.board[toPos[1]][toPos[0]] = fromPiece
            return True

