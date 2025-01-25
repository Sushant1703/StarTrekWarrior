import pygame
import sys

PLAYER_IMG = r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\player.png"
ENEMY_IMG = r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\enemy.jpg"
COIN_IMG = r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\coin.png"
BG_IMG = r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\background.png"
BG_MUSIC_FILE = r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\background_music.mp3"
CLICK_SOUND = r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\click_sound.mp3"
JUMP_SOUND = r"C:\Users\goyal\OneDrive\Documents\TBGsds\assets\jump_sound.mp3"

def load_image(path, size=None):
    try:
        image = pygame.image.load(path).convert_alpha()
        if size:
            image = pygame.transform.scale(image, size)
        return image
    except pygame.error as e:
        print(f"Unable to load image at {path}: {e}")
        sys.exit()

def load_sound(path):
    try:
        sound = pygame.mixer.Sound(path)
        return sound
    except pygame.error as e:
        print(f"Unable to load sound at {path}: {e}")
        return None

def load_font(font_path=None, size=28):
    try:
        if font_path:
            return pygame.font.Font(font_path, size)
        else:
            return pygame.font.SysFont(None, size)
    except:
        print("Failed to load the specified font. Using default font.")
        return pygame.font.SysFont(None, size)
