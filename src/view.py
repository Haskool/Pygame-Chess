import pygame as pg
from mImage import mImage

"""
    View class - acts as front end for GUI and presents to app
"""
class View:
    def __init__(self):
        self._running = True
        self.size = self.width, self.height = 800, 800
        self.psize = self.pwidth, self.pheight = 100, 100
        self._display_surf = pg.Surface(self.size)
        self.background = None
        self.mImages = []
        self.dragging = None

    # construct all board images (mImages) and define their initial locations
    def on_init(self):
        board = pg.image.load("resources\\board.jpg").convert()
        board = pg.transform.scale(board, self.size)
        self.background = board

        colours = ["w", "b"]
        piecePaths = ["r", "n", "b", "q", "k"]
        row = ["r", "n", "b", "q", "k", "b", "n", "r"]
        for colour in colours:
            y = 0 if colour == "b" else self.height - self.pheight
            for piece in piecePaths:
                for i, pieceName in enumerate(row):
                    if pieceName == piece:
                        x = i * self.pwidth
                        pI = mImage("resources\\{}{}.png".format(colour, piece), (x, y), self.psize)
                        self.mImages.append(pI)

            y = self.pheight if colour == "b" else self.height - 2 * self.pheight
            for x in range(0, self.width, self.pwidth):
                pI = pI = mImage("resources\\{}p.png".format(colour), (x, y), self.psize)
                self.mImages.append(pI)

        self.refresh()

    # decides which piece was clicked (if any) and sets the dragging field to it
    def setSelectedPiece(self, mousePos):
        for image in self.mImages:
            if image.isClicked(mousePos):
                self.dragging = image
                return
        self.dragging = None
        
    # performs a drag operation update
    # recentres image so centre aligns with mouse
    def drag(self, coords):
        assert self.dragging != None
        image = self.dragging.image
        coords = tuple(map(lambda a , b : a - b/2, coords, self.dragging.size))
        self.dragging.move(coords)
        self.refresh()

    # re-blits every image to its last updated position
    def refresh(self):
        self._display_surf.blit(self.background, (0, 0))
        for movingI in self.mImages:
            self._display_surf.blit(movingI.image, movingI.pos)