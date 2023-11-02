#python
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rock Paper Scissors")

# Load images
rock_image = pygame.image.load("rock.jpeg")
paper_image = pygame.image.load("paper.jpeg")
scissors_image = pygame.image.load("scissor.png")

# Game loop
running = True
while running:
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Draw the images
    screen.blit(rock_image, (100, 100))
    screen.blit(paper_image, (300, 100))
    screen.blit(scissors_image, (500, 100))
    
    # Update the display
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
