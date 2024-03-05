import pygame
import time
import random

pygame.init()

# Ekran boyutları
width = 800
height = 600

# Renkler
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Yılanın başlangıç konumu ve boyutu
snake_block = 10
snake_speed = 15

# Pencere oluştur
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Yılan Oyunu')

# Zaman kontrolü
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

# Yılanın boyut ve hızı
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, white, [x[0], x[1], snake_block, snake_block])

# Oyun döngüsü
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            pygame.display.update()
            message = font.render("Oyun bitti! Tekrar oynamak için C, çıkmak için Q'ya basın.", True, white)
            game_display.blit(message, [width / 6, height / 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
