"""
    Chess - models the systems of logic involved in a chess game
"""


class Chess:
    def __init__(self):
        self.isWhiteTurn = True
        self.whitePieces = {}
        self.blackPieces = {}

