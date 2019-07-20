class Piece:
    """
        Abstract class that outlines the common methods and fields
        for all chess pieces
    """
    def __init__(self, position):
        self.pos = position
        pass

    def getCanidiateSquares(self):
        raise NotImplementedError

    def move(self, coords):
        self.pos = coords
