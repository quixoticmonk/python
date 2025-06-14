import pygame
import random
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Game settings
FPS = 10
INITIAL_SNAKE_LENGTH = 3

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.reset()
    
    def reset(self):
        # Start snake in the middle of the screen
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        
        self.body = []
        for i in range(INITIAL_SNAKE_LENGTH):
            self.body.append((start_x - i, start_y))
        
        self.direction = Direction.RIGHT
        self.grow_pending = 0
    
    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        self.body.insert(0, new_head)
        
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
    
    def change_direction(self, new_direction):
        # Prevent moving in opposite direction
        current_dx, current_dy = self.direction.value
        new_dx, new_dy = new_direction.value
        
        if (current_dx, current_dy) != (-new_dx, -new_dy):
            self.direction = new_direction
    
    def grow(self):
        self.grow_pending += 1
    
    def check_collision(self):
        head_x, head_y = self.body[0]
        
        # Check wall collision
        if (head_x < 0 or head_x >= GRID_WIDTH or 
            head_y < 0 or head_y >= GRID_HEIGHT):
            return True
        
        # Check self collision
        if (head_x, head_y) in self.body[1:]:
            return True
        
        return False
    
    def get_head_position(self):
        return self.body[0]

class Food:
    def __init__(self):
        self.position = self.spawn_food()
    
    def spawn_food(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)
    
    def respawn(self, snake_body):
        while True:
            new_position = self.spawn_food()
            if new_position not in snake_body:
                self.position = new_position
                break

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
        self.reset_game()
    
    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.paused = False
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                
                elif event.key == pygame.K_p and not self.game_over:
                    self.paused = not self.paused
                
                elif self.game_over and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                    self.reset_game()
                
                elif not self.paused and not self.game_over:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(Direction.DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(Direction.RIGHT)
        
        return True
    
    def update(self):
        if self.game_over or self.paused:
            return
        
        self.snake.move()
        
        # Check food collision
        if self.snake.get_head_position() == self.food.position:
            self.snake.grow()
            self.score += 10
            self.food.respawn(self.snake.body)
        
        # Check game over conditions
        if self.snake.check_collision():
            self.game_over = True
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw snake
        for i, segment in enumerate(self.snake.body):
            x, y = segment
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if i == 0:  # Head
                pygame.draw.rect(self.screen, GREEN, rect)
                pygame.draw.rect(self.screen, DARK_GREEN, rect, 2)
            else:  # Body
                pygame.draw.rect(self.screen, DARK_GREEN, rect)
                pygame.draw.rect(self.screen, GREEN, rect, 1)
        
        # Draw food
        food_x, food_y = self.food.position
        food_rect = pygame.Rect(food_x * CELL_SIZE, food_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.ellipse(self.screen, RED, food_rect)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw pause message
        if self.paused:
            pause_text = self.big_font.render("PAUSED", True, WHITE)
            pause_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(pause_text, pause_rect)
            
            instruction_text = self.font.render("Press P to resume", True, WHITE)
            instruction_rect = instruction_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
            self.screen.blit(instruction_text, instruction_rect)
        
        # Draw game over screen
        if self.game_over:
            game_over_text = self.big_font.render("GAME OVER", True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
            self.screen.blit(game_over_text, game_over_rect)
            
            final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
            final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(final_score_text, final_score_rect)
            
            restart_text = self.font.render("Press SPACE or ENTER to restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
