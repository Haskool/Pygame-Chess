import numpy as np
import pieces
from pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King
class Chess:
    """
        Models the systems of logic involved in a chess game
        Need to initialise board with pieces
    """

    def __init__(self):
        self.isWhitesTurn = True
        self.whitePieces = {}
        self.blackPieces = {}
        self.board = []
        self.isOver = False

    def on_init(self):
        pass

    def move(self, coords1, coords2):
        piece = board[coords1.y][coords1.x]
        # check for things like check and checkmate
        # check piece is right colour
        # check it can go to coords2
        # check the pieces candidate squares
        # check coords 2 does not have piece of same colour on
        # update board
        # update piece(s)
        pass

