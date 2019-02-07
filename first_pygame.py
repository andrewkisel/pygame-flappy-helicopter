import pygame
import time

black = (0, 0, 0)
white = (255, 255, 255)

# Initializing.
pygame.init()

# Define game surface.
surface_width = 800
surface_height = 500
surface = pygame.display.set_mode((surface_width, surface_height))

# Title
pygame.display.set_caption('Helicopter')

# Tracking time for FPS.
clock = pygame.time.Clock()

# Loading helicopter image
img = pygame.image.load('helicopter.png')


# Handle press any key to continue.
def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
        return event.key
    return None


# Create text objects and return them in addition to rectangles.
def make_text_objs(message, font):
    text_surface = font.render(message, True, white)
    return text_surface, text_surface.get_rect()


# Function to pop up messages on the surface.
def message_surface(message):
    small_text = pygame.font.Font('freesansbold.ttf', 20)
    large_text = pygame.font.Font('freesansbold.ttf', 150)

    # Define and place large text
    title_text_surface, title_text_rectangle = make_text_objs(message, large_text)
    title_text_rectangle.center = surface_width / 2, surface_height / 2
    surface.blit(title_text_surface, title_text_rectangle)

    # Define and place small text
    typ_text_surface, typ_text_rectangle = make_text_objs('Press any key to continue', small_text)
    typ_text_rectangle.center = surface_width / 2, ((surface_height / 2) + 100)
    surface.blit(typ_text_surface, typ_text_rectangle)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() is None:
        clock.tick()

    main()


# Handle game over scenario
def gameover():
    message_surface('Kaboom!')


def helicopter(x, y, image):
    surface.blit(image, (x, y))


def main():
    # Helicopter starting points
    x, y = 150, 200

    # Variable to render helicopter movements along y axis.
    y_move = 0

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
        if y > surface_height - 64 or y < 0:
            gameover()

        # Updating specific areas on the screen. If empty parameters - everything is updated.
        pygame.display.update()
        # Setting FPS
        clock.tick(60)


main()
pygame.quit()
quit()
