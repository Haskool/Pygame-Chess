import pygame as pg
from view import View
from chess import Chess


class Controller:
    def __init__(self):
        self.model = Chess()
        self.view = View()

    def on_init(self):
        self.model.on_init()
        self.view.on_init()

    def select(self):
        # set a piece to be dragged using dragging field in View
        coordinates = pg.mouse.get_pos()
        self.view.setSelectedPiece(coordinates)

    def drag(self):
        # perform a drag operation
        if self.view.dragging != None:
            coordinates = pg.mouse.get_pos()
            self.view.drag(coordinates)

    def drop(self):
        if self.view.dragging != None:
            toCoords = pg.mouse.get_pos()
            fromCoords = self.view.dragging.pos
            toCo = viewCoordsToModelIndex(toCoords, self.view.dragging.size)
            fromCo = viewCoordsToModelIndex(fromCoords, self.view.dragging.size)
            moved = self.model.move(tupleToInt(toCo), tupleToInt(fromCo))
            if moved:
                self.view.drop(toCoords)
            else:
                self.view.drop(self.view.dragging.pos)

            self.view.dragging = None

    def getSurface(self):
        return self.view._display_surf


def viewCoordsToModelIndex(pos, size):
    return tuple(map(lambda a, b: a / b, pos, size))


def tupleToInt(t):
    return (int(t[0]), int(t[1]))
