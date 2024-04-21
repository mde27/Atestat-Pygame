import pygame, sys
import random
import subprocess


# Initialize pygame
pygame.init()

# Define the window size
screen_width = 800
screen_height = 600



# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.SHOWN)

# Set the window title
pygame.display.set_caption("Menu")

# Load images
car_image = pygame.image.load("assets/car.png")
obstacle_image = pygame.image.load("assets/obstacle.png")
background_image = pygame.image.load("assets/background_img.png")


# Define the car properties
car_width = 239
car_height = 210
car_x = screen_width / 2 - car_width / 2
car_y = screen_height - car_height - 10
car_speed = 7

# Define the obstacle properties
obstacle_width = 239
obstacle_height = 210
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 10

# Set the score
score = 0

# Load the font
font = pygame.font.Font(None, 36)

# Define the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
        if car_x < 0:
            car_x = 0
    if keys[pygame.K_RIGHT]:
        car_x += car_speed
        if car_x > screen_width - car_width:
            car_x = screen_width - car_width

    # Move the obstacle
    obstacle_y += obstacle_speed
    if obstacle_y > screen_height:
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacle_y = -obstacle_height
        score += 1
        if score == 20:
            screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.HIDDEN)
            subprocess.call(["python", "car&pac.py"])
            running = False

    # Check for collision
    car_rect = pygame.Rect(car_x, car_y, car_width-330, car_height-20)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width-330, obstacle_height-20)
    if car_rect.colliderect(obstacle_rect):
        screen = pygame.display.set_mode((screen_width, screen_height), flags=pygame.HIDDEN)
        subprocess.call(["python", "jumpy&car.py"])
        sys.exit()
        running = False

    # Draw the screen
    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))  
    screen.blit(car_image, (car_x, car_y))
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if score != 2:
        message = font.render("Go!", True, (255, 255, 255))
    screen.blit(message, (screen_width // 2 - message.get_width() // 2, screen_height // 2 - message.get_height() // 2))


    # Update the screen
    pygame.display.update()

# Quit the game
pygame.quit()
