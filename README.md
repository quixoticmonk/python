# Python - Snake Game

A classic Snake game implementation using Python and Pygame with Q as the pair programmer.

## Features

- Classic Snake gameplay mechanics
- Arrow key controls
- Score tracking
- Pause functionality
- Game over and restart system
- Clean, simple graphics
- 800x600 window size (browser-friendly)

## Requirements

- Python 3.11 or higher
- Pygame 2.0.0 or higher

## Installation

1. Clone or download the game files
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```bash
   python snake_game.py
   ```

2. Use the arrow keys to control the snake:
   - ↑ UP: Move up
   - ↓ DOWN: Move down
   - ← LEFT: Move left
   - → RIGHT: Move right

3. Game Controls:
   - **P**: Pause/Resume game
   - **ESC**: Quit game
   - **SPACE** or **ENTER**: Restart after game over

## Game Rules

- Guide the snake to eat the red food
- Each food eaten increases your score by 10 points
- The snake grows longer with each food consumed
- Avoid hitting the walls or the snake's own body
- The game ends when the snake collides with walls or itself

## Game Features

- **Smooth Movement**: Consistent frame rate for smooth gameplay
- **Collision Detection**: Accurate wall and self-collision detection
- **Score System**: Points awarded for each food consumed
- **Pause Function**: Pause and resume gameplay anytime
- **Restart Option**: Quick restart after game over
- **Visual Feedback**: Clear distinction between snake head, body, and food

## Technical Details

- Window Size: 800x600 pixels
- Grid System: 20x20 pixel cells
- Frame Rate: 10 FPS for classic Snake feel
- Snake starts with 3 segments in the center
- Food spawns randomly, avoiding snake body

## Troubleshooting

If you encounter any issues:

1. Make sure Python 3.11+ is installed
2. Verify Pygame is properly installed: `pip list | grep pygame`
3. Try reinstalling Pygame: `pip uninstall pygame && pip install pygame`

## Controls Summary

| Key | Action |
|-----|--------|
| Arrow Keys | Move snake |
| P | Pause/Resume |
| ESC | Quit game |
| SPACE/ENTER | Restart (after game over) |

Enjoy playing Snake!
