import pygame
from utils import load_image

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_image, patrol_width=100, speed=1.0, enemy_type='patrol'):
        super().__init__()
        self.original_image = load_image(enemy_image, (40, 40))
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.patrol_width = patrol_width
        self.start_x = x
        self.direction = 1
        self.enemy_type = enemy_type
        self.facing_right = True
        self.current_frame = 0
        self.animation_speed = 0.1
        self.animation_frames = []

    def update(self, player=None):
        self.movement(player)
        self.animate()

    def movement(self, player=None):
        if self.enemy_type == 'patrol':
            self.rect.x += self.speed * self.direction
            if abs(self.rect.x - self.start_x) >= self.patrol_width:
                self.direction *= -1
                self.facing_right = not self.facing_right
                self.flip_sprite()
        elif self.enemy_type == 'chaser' and player:
            if self.rect.x < player.rect.x:
                self.rect.x += self.speed
                if not self.facing_right:
                    self.facing_right = True
                    self.flip_sprite()
            elif self.rect.x > player.rect.x:
                self.rect.x -= self.speed
                if self.facing_right:
                    self.facing_right = False
                    self.flip_sprite()

    def flip_sprite(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def animate(self):
        if self.animation_frames:
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.animation_frames):
                self.current_frame = 0
            current_img = self.animation_frames[int(self.current_frame)]
            self.image = current_img
            if not self.facing_right:
                self.image = pygame.transform.flip(current_img, True, False)
