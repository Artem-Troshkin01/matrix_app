import random
import sys

import pygame as pg


class MatrixLetters:
    def __init__(self, app_):
        self.app = app_
        self.letters = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
        self.font_size = 8
        self.font = pg.font.SysFont('arial', self.font_size, bold=True)
        self.column = self.app.width // self.font_size
        self.drops = [1 for i in range(0, self.column)]

    def _draw_symbols(self):
        """Отрисовка символов на экране"""
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            green = (0, 255, 0)
            char_render = self.font.render(char, False, green)
            position = i * self.font_size, (self.drops[i] - 1) * self.font_size
            self.app.surface.blit(char_render, position)
            if self.drops[i] * self.font_size > self.app.height and random.uniform(0, 1) > 0.975:
                self.drops[i] = 0
            self.drops[i] += 1

    def run(self):
        self._draw_symbols()


class MatrixApp:
    """Класс приложения"""

    def __init__(self):
        """Инициализация приложения"""
        self.WINDOW = self.width, self.height = 1000, 700
        pg.init()
        self.screen = pg.display.set_mode(self.WINDOW)
        self.surface = pg.Surface(self.WINDOW, pg.SRCALPHA)
        self.clock = pg.time.Clock()
        self.matrixLetters = MatrixLetters(self)
        self._run()

    def _draw_screen(self):
        """Отрисовка экрана"""
        self.surface.fill((0, 0, 0, 10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0, 0))

    def _run(self):
        while True:
            self._draw_screen()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            pg.display.flip()
            self.clock.tick(40)


if __name__ == '__main__':
    app = MatrixApp()
