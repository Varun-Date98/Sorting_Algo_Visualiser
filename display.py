from re import L
import pygame
from typing import List


class MyDisplay:
    def __init__(self):
        pygame.init()
        self.rectangle_width = 20
        self.window_dim = (500, 400)
        self.star_x, self.start_y = 40, 40
        self.window = pygame.display.set_mode(self.window_dim)

    def show(self, array: List[int]):
        self.window.fill((0, 0, 0))

        for i in range(len(array)):
            pygame.draw.rect(
                self.window,
                (255, 0, 0),
                (self.star_x + 30 * i, self.start_y, self.rectangle_width, array[i]),
            )

        pygame.time.delay(50)
        pygame.display.update()

    def setCaption(self, caption: str):
        pygame.display.set_caption(caption)

    def exit(self):
        pygame.quit()
