import pygame as pg
from mImage import mImage


# View class the display surface presented to the app
class View:
    def __init__(self):
        self._running = True
        self.size = self.width, self.height = 800, 800
        self.psize = self.pwidth, self.pheight = 100, 100
        self._display_surf = pg.Surface(self.size)
        self.background = None
        self.mImages = []
        self.dragging = None

    # note that placement coords of an image is relative to top left corner
    # set board image and initial piece image positions
    def on_init(self):
        board = pg.image.load("resources\\board.jpg").convert()
        board = pg.transform.scale(board, self.size)
        self.background = board
        self._display_surf.blit(board, (0, 0))

        colours = ["w", "b"]
        piecePaths = ["r", "n", "b", "q", "k"]
        row = ["r", "n", "b", "q", "k", "b", "n", "r"]
        for colour in colours:
            y = 0 if colour == "b" else self.height - self.pheight
            # Set major pieces
            for piece in piecePaths:
                for i, pieceName in enumerate(row):
                    if pieceName == piece:
                        x = i * self.pwidth
                        pI = mImage("resources\\{}{}.png".format(colour, piece), (x, y), self.psize)
                        self._display_surf.blit(pI.image, pI.pos)
                        self.mImages.append(pI)

            # Set pawns
            y = self.pheight if colour == "b" else self.height - 2 * self.pheight
            for x in range(0, self.width, self.pwidth):
                pI = pI = mImage("resources\\{}p.png".format(colour), (x, y), self.psize)
                self._display_surf.blit(pI.image, (x, y))
                self.mImages.append(pI)

    # decides which piece was clicked (if any) and sets the dragging field to it
    def setSelectedPiece(self, mousePos):
        for image in self.mImages:
            if image.isClicked(mousePos):
                self.dragging = image
                return
        self.dragging = None
        
    # performs a drag operation update
    def drag(self, coords):
        assert self.dragging != None
        image = self.dragging.image
        self.dragging.move(coords)
        self._display_surf.blit(image, coords)

    def refresh(self):
        pass