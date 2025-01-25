# Star Trek - Warrior of the Multiverse

## Overview
**Star Trek - Warrior of the Multiverse** is a multi-level 2D platformer game built with Python and Pygame. The player navigates through levels, collecting coins and avoiding enemies to progress to higher levels. Each level is increasingly challenging, with unique platforms, enemy positions, and coin placements.

## Features
- **Multiple Levels**: 10 predefined levels, each with unique designs and challenges.
- **Player Abilities**: Smooth controls for moving left/right and jumping.
- **Enemies**: Enemies patrol platforms and interact with the player.
- **Coins**: Collect coins to increase score and complete levels.
- **Music & Sound Effects**: Background music and sound effects enhance the gaming experience.
- **HUD**: Displays score, lives, and current level.
- **Game States**: Includes start screen, instructions, level selection, gameplay, and victory/game over screens.

## Game Structure
The project structure is organized as follows:

```bash
TBGsds/
├── __pycache__/          # Compiled Python files (generated automatically)
├── assets/               # Game assets such as images and sounds
│   ├── background_music.mp3
│   ├── background.png
│   ├── click_sound.mp3
│   ├── coin.png
│   ├── enemy.jpg
│   ├── jump_sound.mp3
│   └── player.png
├── coin.py               # Coin sprite logic
├── enemy.py              # Enemy sprite logic
├── game.py               # Core game logic and main event loop
├── gamestructure.txt     # Text file defining game structure
├── levels.py             # Level definitions and setups
├── main.py               # Entry point for the game
├── platform1.py          # Platform sprite logic
├── player.py             # Player sprite logic
└── utils.py              # Utility functions for reusable logic
```

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Pygame library

Install Pygame using pip:

```bash
pip install pygame
```

## How to Run
1. Clone this repository or download the source code.
2. Navigate to the project directory:

```bash
cd TBGsds
```

3. Run the game:

```bash
python main.py
```

## Controls
- **Arrow Keys**: Move the player left and right.
- **Spacebar**: Jump.
- **P**: Start game (from start screen).
- **I**: View instructions.
- **Q**: Quit the game.
- **R**: Retry (on game over screen).
- **N**: Proceed to the next level (on level complete screen).

## Screenshots
![image](https://github.com/user-attachments/assets/f51452ad-198a-4b09-bbea-a966b4140256)
![image](https://github.com/user-attachments/assets/492f96d3-64b1-4b15-85a5-42e9c36143e1)
![image](https://github.com/user-attachments/assets/d3145226-115c-47a9-8ef6-645b82fe3c29)



## Acknowledgments
- Free assets sourced for images and sounds.
