import pygame
import random
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GROUND_Y = SCREEN_HEIGHT - 50
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)

class GameState(Enum):
    MENU = 1
    RUNNING = 2
    GAME_OVER = 3

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 40
        self.vel_y = 0
        self.is_jumping = False
        self.is_sliding = False
        self.slide_timer = 0
        self.animation_frame = 0
        
    def jump(self):
        if not self.is_jumping and not self.is_sliding:
            self.vel_y = -12
            self.is_jumping = True
            
    def slide(self):
        if not self.is_jumping and not self.is_sliding:
            self.is_sliding = True
            self.slide_timer = 30
            self.height = 20
            
    def update(self):
        # Gravity
        if self.is_jumping:
            self.vel_y += 0.8
            self.y += self.vel_y
            
            if self.y >= GROUND_Y - self.height:
                self.y = GROUND_Y - self.height
                self.is_jumping = False
                self.vel_y = 0
                
        # Handle sliding
        if self.is_sliding:
            self.slide_timer -= 1
            if self.slide_timer <= 0:
                self.is_sliding = False
                self.height = 40
                self.y = GROUND_Y - self.height
                
    def draw(self, screen):
        if self.is_sliding:
            # Draw sliding player
            pygame.draw.rect(screen, BLUE, (self.x, self.y + 20, self.width, self.height))
            pygame.draw.circle(screen, BLUE, (self.x + 5, self.y + 30), 5)
            pygame.draw.circle(screen, BLUE, (self.x + 25, self.y + 30), 5)
        else:
            # Draw standing player
            pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
            pygame.draw.circle(screen, BLUE, (self.x + 8, self.y + 10), 5)
            pygame.draw.circle(screen, BLUE, (self.x + 22, self.y + 10), 5)
            
        # Draw eyes
        pygame.draw.circle(screen, WHITE, (self.x + 8, self.y + 15), 3)
        pygame.draw.circle(screen, WHITE, (self.x + 22, self.y + 15), 3)
        pygame.draw.circle(screen, BLACK, (self.x + 8, self.y + 15), 1)
        pygame.draw.circle(screen, BLACK, (self.x + 22, self.y + 15), 1)
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Obstacle:
    def __init__(self, x, y, width, height, speed, obstacle_type="rock"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.type = obstacle_type
        
    def update(self):
        self.x -= self.speed
        
    def draw(self, screen):
        if self.type == "rock":
            pygame.draw.rect(screen, GRAY, (self.x, self.y, self.width, self.height))
            # Add some texture
            pygame.draw.circle(screen, BLACK, (self.x + 5, self.y + 5), 2)
            pygame.draw.circle(screen, BLACK, (self.x + 15, self.y + 10), 2)
        elif self.type == "log":
            pygame.draw.rect(screen, BROWN, (self.x, self.y, self.width, self.height))
            pygame.draw.line(screen, BLACK, (self.x, self.y + 5), (self.x + self.width, self.y + 5), 2)
            
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Coin:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.radius = 8
        self.speed = speed
        self.collected = False
        
    def update(self):
        self.x -= self.speed
        
    def draw(self, screen):
        if not self.collected:
            pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), self.radius)
            pygame.draw.circle(screen, GOLD, (int(self.x), int(self.y)), self.radius - 2)
            
    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 
                          self.radius * 2, self.radius * 2)

class TempleRunner:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Temple Runner")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
        self.reset_game()
        
    def reset_game(self):
        self.player = Player(100, GROUND_Y - 40)
        self.obstacles = []
        self.coins = []
        self.score = 0
        self.coins_collected = 0
        self.game_state = GameState.MENU
        self.speed = 5
        self.obstacle_timer = 0
        self.coin_timer = 0
        self.bg_scroll = 0
        
    def create_obstacle(self):
        obstacle_type = random.choice(["rock", "log"])
        if obstacle_type == "rock":
            width = 20
            height = 25
            y = GROUND_Y - height
        else:  # log
            width = 40
            height = 15
            y = GROUND_Y - height
            
        self.obstacles.append(Obstacle(SCREEN_WIDTH, y, width, height, self.speed, obstacle_type))
        
    def create_coin(self):
        y = GROUND_Y - random.randint(20, 50)
        self.coins.append(Coin(SCREEN_WIDTH, y, self.speed))
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if self.game_state == GameState.MENU:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                        self.game_state = GameState.RUNNING
                elif self.game_state == GameState.RUNNING:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                    elif event.key == pygame.K_DOWN:
                        self.player.slide()
                elif self.game_state == GameState.GAME_OVER:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                        self.game_state = GameState.MENU
        return True
        
    def update(self):
        if self.game_state != GameState.RUNNING:
            return
            
        # Update player
        self.player.update()
        
        # Spawn obstacles
        if self.obstacle_timer <= 0:
            if random.randint(1, 100) < 30:  # 30% chance to spawn obstacle
                self.create_obstacle()
            self.obstacle_timer = random.randint(60, 120)  # 1-2 seconds at 60 FPS
        else:
            self.obstacle_timer -= 1
            
        # Spawn coins
        if self.coin_timer <= 0:
            if random.randint(1, 100) < 40:  # 40% chance to spawn coin
                self.create_coin()
            self.coin_timer = random.randint(30, 90)  # 0.5-1.5 seconds
        else:
            self.coin_timer -= 1
            
        # Update obstacles and check collisions
        for obstacle in self.obstacles[:]:
            obstacle.update()
            if obstacle.x + obstacle.width < 0:
                self.obstacles.remove(obstacle)
            elif self.player.get_rect().colliderect(obstacle.get_rect()):
                # Check if player is sliding and obstacle is log
                if self.player.is_sliding and obstacle.type == "log":
                    self.obstacles.remove(obstacle)
                else:
                    self.game_state = GameState.GAME_OVER
                    return
                    
        # Update coins and check collection
        for coin in self.coins[:]:
            coin.update()
            if coin.x + coin.radius < 0:
                self.coins.remove(coin)
            elif self.player.get_rect().colliderect(coin.get_rect()) and not coin.collected:
                coin.collected = True
                self.coins.remove(coin)
                self.coins_collected += 1
                self.score += 10
                
        # Increase score over time
        self.score += 1
        
        # Increase difficulty
        if self.score % 500 == 0 and self.score > 0:
            self.speed += 0.5
            for obstacle in self.obstacles:
                obstacle.speed = self.speed
            for coin in self.coins:
                coin.speed = self.speed
                
        # Update background scroll
        self.bg_scroll = (self.bg_scroll - self.speed / 2) % SCREEN_WIDTH
        
    def draw_background(self):
        # Sky gradient
        for i in range(SCREEN_HEIGHT):
            color = (135, 206, 235 - i // 10)
            if i < SCREEN_HEIGHT:
                pygame.draw.line(self.screen, color, (0, i), (SCREEN_WIDTH, i))
                
        # Ground
        pygame.draw.rect(self.screen, BROWN, (0, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_Y))
        pygame.draw.rect(self.screen, (101, 67, 33), (0, GROUND_Y, SCREEN_WIDTH, 5))  # Shadow
        
        # Temple pillars
        pillar_x = self.bg_scroll
        for i in range(4):
            x = pillar_x + i * 250
            if x < SCREEN_WIDTH:
                pygame.draw.rect(self.screen, GRAY, (x, GROUND_Y - 80, 30, 80))
                pygame.draw.rect(self.screen, GRAY, (x + 10, GROUND_Y - 100, 10, 20))
                
    def draw_menu(self):
        self.draw_background()
        
        title = self.big_font.render("TEMPLE RUNNER", True, WHITE)
        title_shadow = self.big_font.render("TEMPLE RUNNER", True, BLACK)
        self.screen.blit(title_shadow, (SCREEN_WIDTH//2 - title.get_width()//2 + 2, 
                                        SCREEN_HEIGHT//2 - 100 + 2))
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 
                                 SCREEN_HEIGHT//2 - 100))
        
        instructions = [
            "Press SPACE to jump",
            "Press DOWN to slide under logs",
            "Collect coins for bonus points!",
            "",
            "Press SPACE to start"
        ]
        
        y_offset = SCREEN_HEIGHT//2 - 20
        for text in instructions:
            instruction_text = self.font.render(text, True, WHITE)
            self.screen.blit(instruction_text, 
                           (SCREEN_WIDTH//2 - instruction_text.get_width()//2, y_offset))
            y_offset += 30
            
    def draw_game_over(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        game_over = self.big_font.render("GAME OVER", True, RED)
        self.screen.blit(game_over, (SCREEN_WIDTH//2 - game_over.get_width()//2, 
                                    SCREEN_HEIGHT//2 - 100))
                                    
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 
                                     SCREEN_HEIGHT//2 - 20))
                                     
        coins_text = self.font.render(f"Coins: {self.coins_collected}", True, YELLOW)
        self.screen.blit(coins_text, (SCREEN_WIDTH//2 - coins_text.get_width()//2, 
                                     SCREEN_HEIGHT//2 + 10))
                                     
        restart_text = self.font.render("Press SPACE to return to menu", True, WHITE)
        self.screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, 
                                       SCREEN_HEIGHT//2 + 60))
        
    def draw(self):
        self.draw_background()
        
        if self.game_state == GameState.RUNNING:
            # Draw coins
            for coin in self.coins:
                coin.draw(self.screen)
                
            # Draw obstacles
            for obstacle in self.obstacles:
                obstacle.draw(self.screen)
                
            # Draw player
            self.player.draw(self.screen)
            
            # Draw UI
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            
            coins_text = self.font.render(f"Coins: {self.coins_collected}", True, YELLOW)
            self.screen.blit(coins_text, (10, 50))
            
            speed_text = self.font.render(f"Speed: {int(self.speed * 10)}", True, WHITE)
            self.screen.blit(speed_text, (10, 90))
            
        elif self.game_state == GameState.MENU:
            self.draw_menu()
        elif self.game_state == GameState.GAME_OVER:
            self.draw_game_over()
            
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
    game = TempleRunner()
    game.run()