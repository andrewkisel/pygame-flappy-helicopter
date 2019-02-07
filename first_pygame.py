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


def helicopter(x, y, image):
    surface.blit(img, (x, y))


img = pygame.image.load('helicopter.png')
# Helicopter starting points
x, y = 150, 200

game_over = False

# Game loop
while not game_over:
    # Looping through events tracked by pygame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    surface.fill(black)
    helicopter(x, y, img)
    # Updating specific areas on the screen. If empty parameters - everything is updated.
    pygame.display.update()
    # Setting FPS
    clock.tick(60)

pygame.quit()
quit()
