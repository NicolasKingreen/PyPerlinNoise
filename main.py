import pygame
from pygame.locals import *

from perlin_noise import PerlinNoise

import sys


SCR_SIZE = SCR_W, SCR_H = 800, 800
TARGET_FPS = 30


class Application:
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Perlin Noise")
        self.display_surface = pygame.display.set_mode(SCR_SIZE)

        self.noise = PerlinNoise()

    def update(self):
        pass

    def draw(self):
        self.display_surface.fill("white")
        for x in range(SCR_W):
            for y in range(SCR_H):
                noise_value = (abs(self.noise([x/SCR_W, y/SCR_H])) * 100) % 1
                color = tuple([noise_value * 255] * 3)
                self.display_surface.set_at((x, y), color)
        pygame.display.update()

    def run(self):
        self.is_running = True
        self.draw()
        while self.is_running:

            frame_time_ms = self.clock.tick(TARGET_FPS)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.terminate()

            self.update()

        pygame.quit()
        sys.exit()

    def terminate(self):
        self.is_running = False

if __name__ == "__main__":
    Application().run()
