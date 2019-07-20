from view import View
from chess import Chess
import pygame as pg
from pygame.locals import *

"""
    App - main application
"""
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._view = View()

    def on_init(self):
        pg.init()
        self._display_surf = pg.display.set_mode(self._view.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self._running = True
        self._view.on_init()

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False
        elif event.type == MOUSEBUTTONDOWN:
            # set a piece to be dragged using dragging field in View
            coordinates = pg.mouse.get_pos()
            mImage = self._view.setSelectedPiece(coordinates)
        elif event.type == MOUSEMOTION:
            # perform a drag operation
            if self._view.dragging != None:
                coordinates = pg.mouse.get_pos()
                self._view.drag(coordinates)
        elif event.type == MOUSEBUTTONUP:
            # reset dragging field in View
            if self._view.dragging != None:
                coordinates = pg.mouse.get_pos()
                self._view.drop(coordinates)
                self._view.dragging = None

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(self._view._display_surf, (0, 0))
        pg.display.update()

    def on_cleanup(self):
        pg.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
