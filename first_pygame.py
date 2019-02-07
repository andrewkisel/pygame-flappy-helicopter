import pygame

# Initializing.
pygame.init()
# Define game surface.
surface = pygame.display.set_mode((800, 400))
# Title
pygame.display.set_caption('Helicopter')
# Tracking time for FPS.
clock = pygame.time.Clock()

# Game loop
game_over = False

while not game_over:
    # Looping through events tracked by pygame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Updating specific areas on the screen. If empty parameters - everything is updated.
    pygame.display.update()
    # Setting FPS
    clock.tick(60)

pygame.quit()
quit()
