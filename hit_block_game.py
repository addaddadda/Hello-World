# This is the main file of the game.
from random import randint
import pygame

# Initialize the game
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game window
pygame.display.set_caption("Hit Block Game")

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set the font
font = pygame.font.Font(None, 36)

# Set the clock
clock = pygame.time.Clock()

# Set the game variables
score = 0
game_over = False

# Define the game objects
class Block:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed

    def collide(self, other):
        if self.x < other.x + other.width and self.x + self.width > other.x and self.y < other.y + other.height and self.y + self.height > other.y:
            return True
        else:
            return False

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x < screen_width - self.width:
            self.x += self.speed

    def collide(self, other):
        if self.x < other.x + other.width and self.x + self.width > other.x and self.y < other.y + other.height and self.y + self.height > other.y:
            return True
        else:
            return False

# Create the game objects
block_list = []
for i in range(10):
    # Create 10 blocks with random positions and colors
    # The blocks will appear at the top of the screen and move downwards
    block_list.append(Block(randint(0, screen_width - 50), randint(0, screen_height - 50), 50, 50, white))


player = Player(200, 500, 50, 50, red)

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()

    # Draw the background
    screen.fill(black)

    # Draw the blocks
    for block in block_list:
        block.draw(screen)
        block.move()
        if block.y > screen_height:
            block_list.remove(block)
            score += 1

    # Draw the player
    player.draw(screen)

    # Draw the score
    text = font.render("Score: " + str(score), True, white)
    screen.blit(text, (10, 10))

    # Check for collisions
    for block in block_list:
        if player.collide(block):
            game_over = True

    # Update the screen
    pygame.display.update()

    # Set the clock
    clock.tick(60)

    # Check if the game is over
    if game_over:
        text = font.render("Game Over", True, white)
        screen.blit(text, (200, 250))
        pygame.display.update()
        pygame.time.wait(3000)