from view import View
from chess import Chess
import pygame as pg
from pygame.locals import *


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._view = View()

    def on_init(self):
        pg.init()
        self._display_surf = pg.display.set_mode(self._view.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self._view.on_init()
        self._running = True
        self._display_surf.blit(self._view._display_surf, (0, 0))
        pg.display.update()

    def on_event(self, event):
        if event.type == pg.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

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
