# Snake Game Development System Prompt

## Objective
Create a classic Snake game using Python and pygame that runs in a small browser-sized window with arrow key controls.

## Technical Requirements

### Core Game Mechanics
- Implement a snake that moves continuously in the current direction
- Snake grows longer when eating food
- Game ends when snake collides with walls or itself
- Score tracking based on food consumed
- Food spawns randomly on the game grid

### Display Specifications
- Window size: 800x600 pixels (small browser window size)
- Grid-based movement system (20x20 pixel cells recommended)
- Clean, simple graphics with contrasting colors
- Display current score on screen
- Show game over screen with final score

### Controls
- Arrow keys for directional movement:
  - UP arrow: Move snake up
  - DOWN arrow: Move snake down
  - LEFT arrow: Move snake left
  - RIGHT arrow: Move snake right
- Prevent reverse direction (snake can't immediately go backwards)
- ESC key to quit game
- SPACE or ENTER to restart after game over

### Game Features
- Smooth, consistent movement speed (adjustable frame rate)
- Visual distinction between snake head, body, and food
- Border walls that cause collision
- Pause functionality (P key)
- High score persistence (optional)

## Implementation Guidelines

### Code Structure
- Use object-oriented design with separate classes for:
  - Snake (position, movement, growth)
  - Food (spawning, collision detection)
  - Game (main loop, scoring, state management)
- Modular functions for game logic separation
- Clean, readable code with appropriate comments

### Performance Considerations
- Efficient collision detection
- Optimized rendering (only update changed areas if needed)
- Consistent frame rate (30-60 FPS)
- Memory-efficient snake body tracking

### Visual Design
- Snake: Green rectangles with darker green outline
- Food: Red circle or apple sprite
- Background: Dark color (black or dark blue)
- Score: White text in corner
- Grid lines: Optional, subtle if included

### Error Handling
- Graceful pygame initialization
- Proper event handling
- Clean exit procedures
- Input validation

## Deliverables
1. Complete Python file with pygame implementation
2. Requirements.txt file listing dependencies
3. README with setup and play instructions
4. Optional: Simple sprite files if using custom graphics

## Success Criteria
- Game runs without errors in a 800x600 window
- Responsive arrow key controls
- Proper collision detection
- Score tracking functionality
- Clean game over and restart mechanics
- Smooth gameplay experience

## Additional Features (Optional Enhancements)
- Sound effects for eating food and game over
- Different difficulty levels (speed adjustment)
- Power-ups or special food items
- Snake skin patterns or themes
- Multiplayer support
- Mobile-friendly touch controls adaptation

Remember to test thoroughly on different systems and ensure pygame dependencies are clearly documented for easy setup.
