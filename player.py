import pygame
from utils import load_image, load_sound

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, platforms, enemies, coins, all_sprites, **kwargs):
        super().__init__()
        self.original_image = load_image(kwargs.get('player_image'), (50, 50))
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = kwargs.get('player_speed', 5)
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = kwargs.get('gravity', 0.5)
        self.jump_strength = kwargs.get('jump_strength', -12)
        self.on_ground = False
        self.platforms = platforms
        self.enemies = enemies
        self.coins = coins
        self.all_sprites = all_sprites
        self.score = 0
        self.lives = kwargs.get('initial_lives', 3)
        self.animation_frames = kwargs.get('player_animations', [])
        self.current_frame = 0
        self.animation_speed = kwargs.get('animation_speed', 0.1)
        self.facing_right = True
        self.jump_sound = load_sound(kwargs.get('jump_sound'))
        self.dead = False

    def update(self, keys):
        if not self.dead:
            self.handle_input(keys)
            self.apply_physics()
            self.check_collisions()
            self.animate()

    def handle_input(self, keys):
        previous_facing_right = self.facing_right
        self.velocity.x = 0
        if keys[pygame.K_LEFT]:
            self.velocity.x = -self.speed
            self.facing_right = False
        if keys[pygame.K_RIGHT]:
            self.velocity.x = self.speed
            self.facing_right = True
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity.y = self.jump_strength
            self.on_ground = False
            if self.jump_sound:
                self.jump_sound.play()
        if self.facing_right != previous_facing_right:
            self.flip_sprite()

    def apply_physics(self):
        self.velocity.y += self.gravity
        if self.velocity.y > 12:
            self.velocity.y = 12
        self.rect.x += self.velocity.x
        self.clamp_within_screen()
        self.collide(self.velocity.x, 0, self.platforms)
        self.rect.y += self.velocity.y
        self.clamp_within_screen()
        self.collide(0, self.velocity.y, self.platforms)

    def clamp_within_screen(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.on_ground = True
            self.velocity.y = 0

    def collide(self, vel_x, vel_y, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        for platform in hits:
            if vel_x > 0:
                self.rect.right = platform.rect.left
            if vel_x < 0:
                self.rect.left = platform.rect.right
            if vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.velocity.y = 0
                self.on_ground = True
            if vel_y < 0:
                self.rect.top = platform.rect.bottom
                self.velocity.y = 0

    def flip_sprite(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def animate(self):
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.animation_frames):
            self.current_frame = 0
        if self.animation_frames:
            current_img = self.animation_frames[int(self.current_frame)]
            self.image = current_img
            if not self.facing_right:
                self.image = pygame.transform.flip(current_img, True, False)

    def check_collisions(self):
        enemy_hits = pygame.sprite.spritecollide(self, self.enemies, False)
        if enemy_hits:
            self.lives -= 1
            if self.lives <= 0:
                self.lives = 0
                self.dead = True
                self.kill()
            else:
                self.reset_position()
        coins_collected = pygame.sprite.spritecollide(self, self.coins, True)
        if coins_collected:
            self.score += len(coins_collected) * 10

    def reset_position(self):
        self.rect.topleft = (100, self.rect.bottom - 50)
        self.velocity = pygame.math.Vector2(0, 0)
