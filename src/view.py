import pygame


class View:
    def __init__(self):
        self._running = True
        self.size = self.width, self.height = 800, 800
        self.psize = self.pwidth, self.pheight = 100, 100
        self._display_surf = pygame.Surface(self.size)

    def on_init(self):
        # set board image
        board = pygame.image.load("resources\\board.jpg").convert()
        board = pygame.transform.scale(board, self.size)
        self._display_surf.blit(board, (0, 0))

        # set pawns
        pawnImage = pygame.image.load("resources\\bp.png").convert_alpha()
        pawn = pygame.transform.scale(pawnImage, self.psize)
        for x in range(0, self.width, self.pwidth):
            y = self.pheight
            self._display_surf.blit(pawn, (x, y))

