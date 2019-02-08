import pygame
import time
import random

# Colors for the game.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 100, 255)

# Initializing.
pygame.init()

surface_width = 800
surface_height = 500
image_height = 25
image_width = 25

# Difficulty setting.
difficulty = 5

# Define game surface.
surface = pygame.display.set_mode((surface_width, surface_height))

# Title
pygame.display.set_caption('Helicopter')

# Tracking time for FPS.
clock = pygame.time.Clock()

# Loading helicopter image
img = pygame.image.load('helicopter.png')


def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score: %s' % str(count), True, blue)
    surface.blit(text, (0, 0))


def blocks(x_block, y_block, block_width, block_height, gap):
    pygame.draw.rect(surface, white, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, white, [x_block, y_block + block_height + gap, block_width, surface_height])


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
    text_surface = font.render(message, True, red)
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

    # Block coordinates and size
    x_block = surface_width
    y_block = 0
    block_width = 75
    block_height = random.randint(0, (surface_height / 2))
    gap = image_height * difficulty

    # How fast the blocks move.
    block_move = difficulty

    # Score variable.
    current_score = 0

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
                    y_move = -difficulty
            # Case when releasing the key.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = difficulty

        y += y_move

        # Fill the background.
        surface.fill(black)
        # Put a helicopter icon on the surface.
        helicopter(x, y, img)

        # Update score.
        score(current_score)

        blocks(x_block, y_block, block_width, block_height, gap)
        # Move blocks.
        x_block -= block_move

        # Check if helicopter went out of boundaries.
        if y > surface_height - image_height or y < -image_height:
            gameover()
        # Check if block has moved out of the screen.
        if x_block < (-1 * block_width):
            # Resetting the starting x-position of the block.
            x_block = surface_width
            block_height = random.randint(0, (surface_height / 2))

        # Check if we crashed into the block.
        if x + image_width > x_block:
            if x < x_block + block_width:
                # print('Possibly within the boundaries of x')
                if y < block_height:
                    # print('y crossover upper!')
                    if x - image_width < block_width + x_block:
                        # print('game over. hit upper.')
                        gameover()
            if y + image_height > block_height + gap:
                # print('y crossover lower')
                if x < block_width + x_block:
                    # print('Game over lower')
                    gameover()

        # Update score when you passed the gap.
        if x < x_block + 1 and x > x_block - block_move:
            current_score += 1

        # Updating specific areas on the screen. If empty parameters - everything is updated.
        pygame.display.update()
        # Setting FPS
        clock.tick(60)


main()
pygame.quit()
quit()
