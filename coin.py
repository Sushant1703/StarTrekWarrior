import pygame
from utils import load_image

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, coin_image, animation_speed=0.2):
        super().__init__()
        self.original_image = load_image(coin_image, (30, 30))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_index = 0
        self.animation_speed = animation_speed
        self.animation_frames = [
            pygame.transform.rotate(self.original_image, angle)
            for angle in range(0, 360, 30)
        ]

    def update(self):
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.animation_frames):
            self.animation_index = 0
        self.image = self.animation_frames[int(self.animation_index)]
