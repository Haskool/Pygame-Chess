class Chess:
    """
        sChess - models the systems of logic involved in a chess game
    """
    def __init__(self):
        self.isWhiteTurn = True
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

