import pygame
import sys  
import os
from utils import (
    load_image, load_sound, PLAYER_IMG, ENEMY_IMG, COIN_IMG,
    BG_IMG, BG_MUSIC_FILE, CLICK_SOUND, JUMP_SOUND
)
from platform1 import Platform
from player import Player
from enemy import Enemy
from coin import Coin

class Game:
    def __init__(self):
        pygame.init()

       
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.FPS = 60

       
        self.BG_COLOR = (135, 206, 250)  

        self.FONT = pygame.font.SysFont(None, 28)

       
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Star Trek - Warrior of the Multiverse")
        self.clock = pygame.time.Clock()
        self.running = True

        self.background = load_image(BG_IMG, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
       
        self.click_sound = load_sound(CLICK_SOUND)
        self.jump_sound = load_sound(JUMP_SOUND)
      
        self.start_music()

        self.state = 'start_screen'

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.player = None

        self.level = 1
        self.max_level = 10
        self.level_access = [True] + [False] * (self.max_level - 1) 

        self.levels = self.define_levels()

    def start_music(self):
        if os.path.exists(BG_MUSIC_FILE):
            pygame.mixer.music.load(BG_MUSIC_FILE)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
        else:
            print("Background music file not found.")

    def define_levels(self):

        return {
            1: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (100, 450, 100, 20)},
                    {'rect': (250, 350, 100, 20)},
                    {'rect': (400, 250, 100, 20)},
                    {'rect': (550, 150, 100, 20)},
                    {'rect': (700, 50, 100, 20)},
                ],
                'enemies': [
                    {'x': 100, 'y': 410, 'type': 'patrol', 'speed': 1.5},
                    {'x': 250, 'y': 310, 'type': 'patrol', 'speed': 1.5},
                    {'x': 400, 'y': 210, 'type': 'chaser', 'speed': 1.0},
                    {'x': 550, 'y': 110, 'type': 'chaser', 'speed': 1.0},
                ],
                'coins': [
                    (130, 420),
                    (280, 320),
                    (430, 220),
                    (580, 120),
                    (730, 20),
                ],
                'background': BG_IMG,
            },
            2: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (150, 450, 100, 20)},
                    {'rect': (300, 350, 100, 20)},
                    {'rect': (450, 250, 100, 20)},
                    {'rect': (600, 150, 100, 20)},
                    {'rect': (750, 50, 100, 20)},
                ],
                'enemies': [
                    {'x': 150, 'y': 410, 'type': 'patrol', 'speed': 1.5},
                    {'x': 300, 'y': 310, 'type': 'chaser', 'speed': 1.0},
                    {'x': 450, 'y': 210, 'type': 'patrol', 'speed': 1.5},
                    {'x': 600, 'y': 110, 'type': 'chaser', 'speed': 1.0},
                ],
                'coins': [
                    (180, 420),
                    (330, 320),
                    (480, 220),
                    (630, 120),
                    (780, 20),
                ],
                'background': BG_IMG,
            },
            3: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (200, 450, 100, 20)},
                    {'rect': (350, 350, 100, 20)},
                    {'rect': (500, 250, 100, 20)},
                    {'rect': (650, 150, 100, 20)},
                    {'rect': (300, 150, 100, 20)},
                ],
                'enemies': [
                    {'x': 200, 'y': 410, 'type': 'patrol', 'speed': 1.5},
                    {'x': 350, 'y': 310, 'type': 'chaser', 'speed': 1.0},
                    {'x': 500, 'y': 210, 'type': 'patrol', 'speed': 1.5},
                    {'x': 650, 'y': 110, 'type': 'chaser', 'speed': 1.0},
                ],
                'coins': [
                    (230, 420),
                    (380, 320),
                    (530, 220),
                    (680, 120),
                    (330, 140),
                ],
                'background': BG_IMG,
            },
            4: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (50, 450, 100, 20)},
                    {'rect': (200, 350, 100, 20)},
                    {'rect': (350, 250, 100, 20)},
                    {'rect': (500, 150, 100, 20)},
                    {'rect': (650, 50, 100, 20)},
                    {'rect': (400, 50, 100, 20)},
                ],
                'enemies': [
                    {'x': 50, 'y': 410, 'type': 'patrol', 'speed': 1.5},
                    {'x': 200, 'y': 310, 'type': 'chaser', 'speed': 1.0},
                    {'x': 350, 'y': 210, 'type': 'patrol', 'speed': 1.5},
                    {'x': 500, 'y': 110, 'type': 'chaser', 'speed': 1.0},
                    {'x': 650, 'y': 10, 'type': 'chaser', 'speed': 1.0},
                ],
                'coins': [
                    (80, 420),
                    (230, 320),
                    (380, 220),
                    (530, 120),
                    (680, 20),
                    (430, 20),
                ],
                'background': BG_IMG,
            },
            5: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (100, 450, 100, 20)},
                    {'rect': (250, 350, 100, 20)},
                    {'rect': (400, 250, 100, 20)},
                    {'rect': (550, 150, 100, 20)},
                    {'rect': (700, 50, 100, 20)},
                    {'rect': (300, 50, 100, 20)},
                ],
                'enemies': [
                    {'x': 100, 'y': 410, 'type': 'patrol', 'speed': 1.5},
                    {'x': 250, 'y': 310, 'type': 'chaser', 'speed': 1.0},
                    {'x': 400, 'y': 210, 'type': 'patrol', 'speed': 1.5},
                    {'x': 550, 'y': 110, 'type': 'chaser', 'speed': 1.0},
                    {'x': 700, 'y': 10, 'type': 'chaser', 'speed': 1.0},
                ],
                'coins': [
                    (130, 420),
                    (280, 320),
                    (430, 220),
                    (580, 120),
                    (730, 20),
                    (330, 20),
                ],
                'background': BG_IMG,
            },
            6: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (150, 450, 100, 20)},
                    {'rect': (300, 350, 100, 20)},
                    {'rect': (450, 250, 100, 20)},
                    {'rect': (600, 150, 100, 20)},
                    {'rect': (750, 50, 100, 20)},
                    {'rect': (200, 50, 100, 20)},
                ],
                'enemies': [
                    {'x': 150, 'y': 410, 'type': 'patrol', 'speed': 1.5},
                    {'x': 300, 'y': 310, 'type': 'chaser', 'speed': 1.0},
                    {'x': 450, 'y': 210, 'type': 'patrol', 'speed': 1.5},
                    {'x': 600, 'y': 110, 'type': 'chaser', 'speed': 1.0},
                    {'x': 750, 'y': 10, 'type': 'chaser', 'speed': 1.0},
                    {'x': 200, 'y': 10, 'type': 'patrol', 'speed': 1.5},
                ],
                'coins': [
                    (180, 420),
                    (330, 320),
                    (480, 220),
                    (630, 120),
                    (780, 20),
                    (230, 20),
                ],
                'background': BG_IMG,
            },
            7: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (50, 450, 100, 20)},
                    {'rect': (200, 350, 100, 20)},
                    {'rect': (350, 250, 100, 20)},
                    {'rect': (500, 150, 100, 20)},
                    {'rect': (650, 50, 100, 20)},
                    {'rect': (400, 50, 100, 20)},
                ],
                'enemies': [
                    {'x': 50, 'y': 410, 'type': 'patrol', 'speed': 1.5},
                    {'x': 200, 'y': 310, 'type': 'chaser', 'speed': 1.0},
                    {'x': 350, 'y': 210, 'type': 'patrol', 'speed': 1.5},
                    {'x': 500, 'y': 110, 'type': 'chaser', 'speed': 1.0},
                    {'x': 650, 'y': 10, 'type': 'chaser', 'speed': 1.0},
                    {'x': 400, 'y': 10, 'type': 'patrol', 'speed': 1.5},
                ],
                'coins': [
                    (80, 420),
                    (230, 320),
                    (380, 220),
                    (530, 120),
                    (680, 20),
                    (430, 20),
                ],
                'background': BG_IMG,
            },
            8: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (100, 450, 100, 20)},
                    {'rect': (250, 350, 100, 20)},
                    {'rect': (400, 250, 100, 20)},
                    {'rect': (550, 150, 100, 20)},
                    {'rect': (700, 50, 100, 20)},
                    {'rect': (300, 50, 100, 20)},
                ],
                'enemies': [
                    {'x': 100, 'y': 410, 'type': 'patrol', 'speed': 1.5},
                    {'x': 250, 'y': 310, 'type': 'chaser', 'speed': 1.0},
                    {'x': 400, 'y': 210, 'type': 'patrol', 'speed': 1.5},
                    {'x': 550, 'y': 110, 'type': 'chaser', 'speed': 1.0},
                    {'x': 700, 'y': 10, 'type': 'chaser', 'speed': 1.0},
                    {'x': 300, 'y': 10, 'type': 'patrol', 'speed': 1.5},
                ],
                'coins': [
                    (130, 420),
                    (280, 320),
                    (430, 220),
                    (580, 120),
                    (730, 20),
                    (330, 20),
                ],
                'background': BG_IMG,
            },
            9: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (150, 450, 100, 20)},
                    {'rect': (300, 350, 100, 20)},
                    {'rect': (450, 250, 100, 20)},
                    {'rect': (600, 150, 100, 20)},
                    {'rect': (750, 50, 100, 20)},
                    {'rect': (200, 50, 100, 20)},
                    {'rect': (350, 50, 100, 20)},
                ],
                'enemies': [
                    {'x': 150, 'y': 410, 'type': 'patrol', 'speed': 1.5},
                    {'x': 300, 'y': 310, 'type': 'chaser', 'speed': 1.0},
                    {'x': 450, 'y': 210, 'type': 'patrol', 'speed': 1.5},
                    {'x': 600, 'y': 110, 'type': 'chaser', 'speed': 1.0},
                    {'x': 750, 'y': 10, 'type': 'chaser', 'speed': 1.0},
                    {'x': 200, 'y': 10, 'type': 'patrol', 'speed': 1.5},
                    {'x': 350, 'y': 10, 'type': 'patrol', 'speed': 1.5},
                ],
                'coins': [
                    (180, 420),
                    (330, 320),
                    (480, 220),
                    (630, 120),
                    (780, 20),
                    (230, 20),
                    (380, 20),
                ],
                'background': BG_IMG,
            },
            10: {
                'platforms': [
                    {'rect': (0, 550, 800, 50)},
                    {'rect': (100, 450, 100, 20)},
                    {'rect': (250, 350, 100, 20)},
                    {'rect': (400, 250, 100, 20)},
                    {'rect': (550, 150, 100, 20)},
                    {'rect': (700, 50, 100, 20)},
                    {'rect': (200, 50, 100, 20)},
                    {'rect': (350, 50, 100, 20)},
                    {'rect': (500, 50, 100, 20)},
                    {'rect': (650, 50, 100, 20)},
                ],
                'enemies': [
                    {'x': 100, 'y': 410, 'type': 'patrol', 'speed': 1.5},
                    {'x': 250, 'y': 310, 'type': 'chaser', 'speed': 1.0},
                    {'x': 400, 'y': 210, 'type': 'patrol', 'speed': 1.5},
                    {'x': 550, 'y': 110, 'type': 'chaser', 'speed': 1.0},
                    {'x': 700, 'y': 10, 'type': 'chaser', 'speed': 1.0},
                    {'x': 200, 'y': 10, 'type': 'patrol', 'speed': 1.5},
                    {'x': 350, 'y': 10, 'type': 'patrol', 'speed': 1.5},
                    {'x': 500, 'y': 10, 'type': 'patrol', 'speed': 1.5},
                    {'x': 650, 'y': 10, 'type': 'patrol', 'speed': 1.5},
                ],
                'coins': [
                    (130, 420),
                    (280, 320),
                    (430, 220),
                    (580, 120),
                    (730, 20),
                    (230, 20),
                    (380, 20),
                    (530, 20),
                    (680, 20),
                ],
                'background': BG_IMG,
            },
        }

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            if self.state == 'start_screen':
                self.show_start_screen()
            elif self.state == 'instructions':
                self.show_instructions()
            elif self.state == 'level_selection':
                self.show_level_selection()
            elif self.state == 'gameplay':
                self.handle_gameplay_events()
                self.update_gameplay()
                self.draw_gameplay()
            elif self.state == 'level_complete':
                self.show_level_complete()
            elif self.state == 'game_over':
                self.show_game_over()
            elif self.state == 'victory':
                self.show_victory_screen()
        self.quit_game()

    def handle_gameplay_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

    def update_gameplay(self):
        keys = pygame.key.get_pressed()
        if self.player:
            self.player.update(keys)
        self.enemies.update(self.player)

        self.coins.update()

        if not self.player or not self.player.alive():
            self.state = 'game_over'

        elif len(self.coins) == 0:
            if self.level < self.max_level:
                self.state = 'level_complete'
            else:
                self.state = 'victory'

    def draw_gameplay(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)

        score_text = self.FONT.render(f"Score: {self.player.score}", True, (255, 255, 255))
        lives_text = self.FONT.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        level_text = self.FONT.render(f"Level: {self.level}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 40))
        self.screen.blit(level_text, (10, 70))

        pygame.display.flip()

    def show_start_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if self.click_sound:
                        self.click_sound.play()
                    self.state = 'level_selection'
                if event.key == pygame.K_i:
                    if self.click_sound:
                        self.click_sound.play()
                    self.state = 'instructions'
                if event.key == pygame.K_q:
                    if self.click_sound:
                        self.click_sound.play()
                    self.quit_game()

        self.screen.blit(self.background, (0, 0))
        title = self.FONT.render("Welcome to Star Trek - Warrior of the Multiverse!", True, (255, 255, 255))
        play_button = self.FONT.render("Press 'P' to Play", True, (255, 255, 255))
        instructions = self.FONT.render("Press 'I' for Instructions", True, (255, 255, 255))
        quit_button = self.FONT.render("Press 'Q' to Quit", True, (255, 255, 255))

        self.screen.blit(title, (self.SCREEN_WIDTH // 2 - title.get_width() // 2, 150))
        self.screen.blit(play_button, (self.SCREEN_WIDTH // 2 - play_button.get_width() // 2, 250))
        self.screen.blit(instructions, (self.SCREEN_WIDTH // 2 - instructions.get_width() // 2, 300))
        self.screen.blit(quit_button, (self.SCREEN_WIDTH // 2 - quit_button.get_width() // 2, 350))
        pygame.display.flip()

    def show_instructions(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    if self.click_sound:
                        self.click_sound.play()
                    self.state = 'start_screen'

        self.screen.blit(self.background, (0, 0))
        instructions = [
            "Instructions:",
            "1. Use LEFT and RIGHT arrow keys to move.",
            "2. Press SPACE to jump.",
            "3. Avoid enemies.",
            "4. Collect coins to increase your score.",
            "5. Collect all coins to complete the level.",
            "6. You have 3 lives per level.",
            "Press 'B' to go back."
        ]

        for i, line in enumerate(instructions):
            text = self.FONT.render(line, True, (255, 255, 255))
            self.screen.blit(text, (50, 100 + i * 40))

        pygame.display.flip()

    def show_level_selection(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                selected_level = None
 
                if event.key in [pygame.K_1, pygame.K_KP1] and self.level_access[0]:
                    selected_level = 1
                elif event.key in [pygame.K_2, pygame.K_KP2] and self.level_access[1]:
                    selected_level = 2
                elif event.key in [pygame.K_3, pygame.K_KP3] and self.level_access[2]:
                    selected_level = 3
                elif event.key in [pygame.K_4, pygame.K_KP4] and self.level_access[3]:
                    selected_level = 4
                elif event.key in [pygame.K_5, pygame.K_KP5] and self.level_access[4]:
                    selected_level = 5
                elif event.key in [pygame.K_6, pygame.K_KP6] and self.level_access[5]:
                    selected_level = 6
                elif event.key in [pygame.K_7, pygame.K_KP7] and self.level_access[6]:
                    selected_level = 7
                elif event.key in [pygame.K_8, pygame.K_KP8] and self.level_access[7]:
                    selected_level = 8
                elif event.key in [pygame.K_9, pygame.K_KP9] and self.level_access[8]:
                    selected_level = 9
                elif event.key in [pygame.K_0, pygame.K_KP0] and self.level_access[9]:
                    selected_level = 10
                elif event.key == pygame.K_b:
                    if self.click_sound:
                        self.click_sound.play()
                    self.state = 'start_screen'

                if selected_level:
                    if self.click_sound:
                        self.click_sound.play()
                    self.level = selected_level
                    self.init_level()
                    self.state = 'gameplay'
                if event.key == pygame.K_ESCAPE:
                    if self.click_sound:
                        self.click_sound.play()
                    self.state = 'start_screen'

        self.screen.blit(self.background, (0, 0))
        title = self.FONT.render("Select a Level", True, (255, 255, 255))
        self.screen.blit(title, (self.SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

        for i in range(self.max_level):
            level_num = i + 1
            level_text = f"Level {level_num}"
            color = (0, 255, 0) if self.level_access[i] else (128, 128, 128)
            text = self.FONT.render(level_text, True, color)
            self.screen.blit(text, (self.SCREEN_WIDTH // 2 - text.get_width() // 2, 150 + i * 40))

        back_text = self.FONT.render("Press 'B' to Go Back", True, (255, 255, 255))
        self.screen.blit(back_text, (self.SCREEN_WIDTH // 2 - back_text.get_width() // 2, 150 + self.max_level * 40 + 20))

        pygame.display.flip()

    def init_level(self):

        self.all_sprites.empty()
        self.platforms.empty()
        self.enemies.empty()
        self.coins.empty()

        level_data = self.levels.get(self.level, None)
        if not level_data:
            print(f"Level {self.level} data not found.")
            self.state = 'game_over'
            return

        for plat in level_data['platforms']:
            platform = Platform(
                plat['rect'][0], plat['rect'][1],
                plat['rect'][2], plat['rect'][3],
                moving=plat.get('moving', False),
                move_range=plat.get('move_range', 100),
                speed=plat.get('speed', 2),
                axis=plat.get('axis', 'horizontal')
            )
            self.all_sprites.add(platform)
            self.platforms.add(platform)

        if not self.player:
            self.player = Player(
                100, self.SCREEN_HEIGHT - 100,
                self.platforms, self.enemies, self.coins,
                self.all_sprites,
                player_image=PLAYER_IMG,
                player_speed=5, 
                gravity=0.5,      
                jump_strength=-12, 
                initial_lives=3,
                jump_sound=JUMP_SOUND
            )
            self.all_sprites.add(self.player)
        else:
            self.player.lives = 3
            self.player.score = 0
            self.player.dead = False 
            self.player.rect.topleft = (100, self.SCREEN_HEIGHT - 100)
            self.player.velocity = pygame.math.Vector2(0, 0)
            self.all_sprites.add(self.player)

        for enemy_data in level_data['enemies']:
            enemy = Enemy(
                enemy_data['x'], enemy_data['y'],
                ENEMY_IMG,
                patrol_width=enemy_data.get('patrol_width', 100),
                speed=enemy_data.get('speed', 1.0), 
                enemy_type=enemy_data.get('type', 'patrol')
            )
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

        for coin_pos in level_data['coins']:
            coin = Coin(coin_pos[0], coin_pos[1], COIN_IMG)
            self.all_sprites.add(coin)
            self.coins.add(coin)

    def show_level_complete(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    if self.click_sound:
                        self.click_sound.play()
                    self.level += 1
                    if self.level > self.max_level:
                        self.state = 'victory'
                    else:
                        if self.level <= self.max_level:
                            self.level_access[self.level - 1] = True
                        self.init_level()
                        self.state = 'gameplay'
                if event.key == pygame.K_q:
                    if self.click_sound:
                        self.click_sound.play()
                    self.quit_game()

        self.screen.blit(self.background, (0, 0))
        complete_text = self.FONT.render(f"Level {self.level} Complete!", True, (0, 255, 0))
        next_text = self.FONT.render("Press 'N' for Next Level or 'Q' to Quit", True, (255, 255, 255))
        self.screen.blit(complete_text, (self.SCREEN_WIDTH // 2 - complete_text.get_width() // 2, 200))
        self.screen.blit(next_text, (self.SCREEN_WIDTH // 2 - next_text.get_width() // 2, 250))
        pygame.display.flip()

    def show_game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if self.click_sound:
                        self.click_sound.play()
                    self.init_level()
                    self.state = 'gameplay'
                if event.key == pygame.K_q:
                    if self.click_sound:
                        self.click_sound.play()
                    self.quit_game()

        self.screen.blit(self.background, (0, 0))
        game_over_text = self.FONT.render("Game Over!", True, (255, 0, 0))
        retry_text = self.FONT.render("Press 'R' to Retry or 'Q' to Quit", True, (255, 255, 255))
        self.screen.blit(game_over_text, (self.SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 200))
        self.screen.blit(retry_text, (self.SCREEN_WIDTH // 2 - retry_text.get_width() // 2, 250))
        pygame.display.flip()

    def show_victory_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if self.click_sound:
                        self.click_sound.play()
                    self.level = 1
                    self.level_access = [True] + [False] * (self.max_level - 1)
                    self.init_level()
                    self.state = 'gameplay'
                if event.key == pygame.K_q:
                    if self.click_sound:
                        self.click_sound.play()
                    self.quit_game()

        self.screen.blit(self.background, (0, 0))
        victory_text = self.FONT.render("Congratulations! You Won!", True, (0, 255, 0))
        retry_text = self.FONT.render("Press 'P' to Play Again or 'Q' to Quit", True, (255, 255, 255))
        self.screen.blit(victory_text, (self.SCREEN_WIDTH // 2 - victory_text.get_width() // 2, 200))
        self.screen.blit(retry_text, (self.SCREEN_WIDTH // 2 - retry_text.get_width() // 2, 250))
        pygame.display.flip()

    def quit_game(self):
        pygame.quit()
        sys.exit()
