import pygame

black = (0, 0, 0)
white = (255, 255, 255)

# Initializing.
pygame.init()
# Define game surface.
surface = pygame.display.set_mode((800, 400))
# Title
pygame.display.set_caption('Helicopter')
# Tracking time for FPS.
clock = pygame.time.Clock()
# Loading helicopter image
img = pygame.image.load('helicopter.png')
# Helicopter starting points
x, y = 150, 200

# Variable to render helicopter movements along y axis.
y_move = 5


def gameover():
    quit()


def helicopter(x, y, image):
    surface.blit(img, (x, y))


game_over = False

# Game loop
while not game_over:
    # Looping through events tracked by pygame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # Case when pressing a key.
        if event.type == pygame.KEYDOWN:
            # Get specific key that is pressed.
            if event.key == pygame.K_UP:
                y_move = -5
        # Case when releasing the key.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_move = 5

    y += y_move

    # Fill the background.
    surface.fill(black)
    # Put a helicopter icon on the surface.
    helicopter(x, y, img)

    # Check if helicopter went out of boundaries.
    if y > 360 or y < 0:
        gameover()

    # Updating specific areas on the screen. If empty parameters - everything is updated.
    pygame.display.update()
    # Setting FPS
    clock.tick(60)

pygame.quit()
quit()
