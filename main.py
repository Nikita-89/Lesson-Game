import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размеры экрана
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Заголовок окна
pygame.display.set_caption('Snake Game')

# Параметры змейки
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

# Шрифт для отображения текста
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Функция для вывода счета
def display_score(score):
    value = score_font.render(f"Ваш счет: {score}", True, white)
    screen.blit(value, [0, 0])

# Функция для отображения текста
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

# Функция для игры
def game_loop():
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Направление движения змейки
    x1_change = 0
    y1_change = 0

    # Тело змейки
    snake_list = []
    snake_length = 1

    # Координаты еды
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    # Основной игровой цикл
    while not game_over:

        # Если игра завершена, показываем сообщение
        while game_close:
            screen.fill(blue)
            message("Вы проиграли! Нажмите Q для выхода или C для новой игры", red)
            display_score(snake_length - 1)
            pygame.display.update()

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Обработка событий
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

        # Если змейка выходит за пределы экрана — проигрыш
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        # Обновление координат змейки
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        # Отрисовка еды
        pygame.draw.rect(screen, green, [food_x, food_y, snake_block, snake_block])

        # Добавление головы змейки
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Удаление последнего элемента, если змейка не съела еду
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Проверка на столкновение с собственным телом
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Отрисовка змейки
        for block in snake_list:
            pygame.draw.rect(screen, white, [block[0], block[1], snake_block, snake_block])

        # Проверка на поедание еды
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        # Отображение счета
        display_score(snake_length - 1)

        # Обновление экрана
        pygame.display.update()

        # Установка FPS
        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

# Запуск игры
game_loop()
