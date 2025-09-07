# Example file showing a basic pygame "game loop"
import pygame
import random

#screen size
frameSizeX = 800
frameSizeY = 800

# pygame setup
pygame.init()
screen = pygame.display.set_mode((frameSizeX, frameSizeY))
clock = pygame.time.Clock()
running = True
tileSize = 20 # how big do you want the screen? 


food_pos = [random.randint(0, 19), random.randint(0, 19)]
snake_pos = [[3, 2], [4,3]]

# direction is which way the snake goes regardless of user input.
direction = "right"
changeTo = direction # this lets us change where the snake goes.

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #input handling
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo = 'up'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo = 'left'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo = 'right'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo = 'down'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # make sure snake cant go in the wrong direction
    if changeTo == 'up' and direction != 'down':
        direction = 'up'
    elif changeTo == 'down' and direction != 'up':
        direction = 'down'
    elif changeTo == 'right' and direction != 'left':
        direction = 'right'
    elif changeTo == 'left' and direction != 'right':
        direction = 'left'

    #update body pos
    i = 1
    while i < len(snake_pos):
        snake_pos[i][0] = snake_pos[i-1][0]
        snake_pos[i][1] = snake_pos[i-1][1]

    # change pos
    if direction == 'up':
        snake_pos[0][1] -= 1
    elif direction == 'down':
        snake_pos[0][1] += 1
    elif direction == 'right':
        snake_pos[0][0] += 1
    elif direction == 'left':
        snake_pos[0][0] -= 1

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    food = pygame.Rect(food_pos[0]*frameSizeY/tileSize, food_pos[1]*frameSizeY/tileSize, frameSizeX/tileSize, frameSizeY/tileSize)
    pygame.draw.rect(screen, (255, 0, 0), food)

    for bodyPart in snake_pos:
        snake = pygame.Rect(bodyPart[0]*frameSizeY/tileSize, bodyPart[1]*frameSizeY/tileSize, frameSizeX/tileSize, frameSizeY/tileSize)
        pygame.draw.rect(screen, (0,255,0), snake)


    if food_pos[0] == snake_pos[0][0] and food_pos[1] == snake_pos[0][1]:
        food_pos = [random.randint(0, 19), random.randint(0, 19)]
        snake_pos.append([snake_pos[0][0],snake_pos[0][1]])


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(15)  # limits FPS to 60

pygame.quit()