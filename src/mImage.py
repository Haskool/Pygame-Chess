import pygame as pg


class mImage:
    """
        mImage - moveable image
        wrapper for draggable images (pieces)
    """

    def __init__(self, path, pos, size):
        self.path = path
        self.pos = self.x, self.y = pos
        self.size = self.width, self.height = size
        image = pg.image.load(path).convert_alpha()
        self.image = pg.transform.scale(image, size)
        self.dragged = False

    # checks if clicked and sets dragged field
    def isDragged(self, coords):
        assert self.dragged == False
        x = coords[0]
        y = coords[1]
        xInBox = x >= self.x and x <= self.x + self.width
        yInBox = y >= self.y and y <= self.y + self.height
        self.dragged = xInBox and yInBox
        return self.dragged

    # called once user releases mouse click and image was being dragged
    def drop(self):
        assert self.dragged == True
        self.dragged = False

    # updates location fields
    def move(self, newPos):
        self.pos = newPos
        self.x = newPos[0]
        self.y = newPos[1]

