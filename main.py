import pygame
import time
import random

# Initialise pygame
pygame.init()

# defining colours
snake_colour = (255, 255, 255)  # snake colour
background_colour = (0, 0, 0)  # backgorund
game_over_message_colour = (255, 0, 0)  # gaame over message
food_colour = (255, 165, 0)  # food
score_colour = (255, 0, 165)  # score
width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Perry the Python")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)


def draw_score(score):
    text = score_font.render("Score: " + str(score), True, score_colour)
    game_display.blit(text, [0, 0])


def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, snake_colour, [pixel[0], pixel[1], snake_size, snake_size])


def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / 10.0 * 10)
    target_y = round(random.randrange(0, height - snake_size) / 10.0 * 10)

    while not game_over:
        while game_close:
            game_display.fill(background_colour)
            game_over_message = message_font.render("Game Over!", True, game_over_message_colour)
            game_display.blit(game_over_message, [width / 3, height / 3])
            draw_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(background_colour)
        pygame.draw.rect(game_display, food_colour, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True
        draw_snake(snake_size, snake_pixels)
        draw_score(snake_length - 1)

        pygame.display.update()

        radius = 5

        if target_x - radius <= x <= target_x + radius and target_y - radius <= y <= target_y + radius:
            target_x = round(random.randrange(0, width - snake_size) / 10.0 * 10)
            target_y = round(random.randrange(0, height - snake_size) / 10.0 * 10)
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


run_game()
