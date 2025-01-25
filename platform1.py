import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, moving=False, move_range=100, speed=2, axis='horizontal'):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.moving = moving
        self.move_range = move_range
        self.speed = speed
        self.axis = axis
        self.start_pos = pygame.math.Vector2(x, y)
        self.direction = 1

    def update(self):
        if self.moving:
            if self.axis == 'horizontal':
                self.rect.x += self.speed * self.direction
                if abs(self.rect.x - self.start_pos.x) >= self.move_range:
                    self.direction *= -1
            elif self.axis == 'vertical':
                self.rect.y += self.speed * self.direction
                if abs(self.rect.y - self.start_pos.y) >= self.move_range:
                    self.direction *= -1
