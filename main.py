import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Название игры
pygame.display.set_caption("Игра на выживание")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Квадрат 50x50
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

# Класс врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Квадрат 50x50
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 50)
        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Поменять направление при столкновении со стенами
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speed_x *= -1
        if self.rect.bottom >= SCREEN_HEIGHT or self.rect.top <= 0:
            self.speed_y *= -1

# Функция для создания врагов
def create_enemies(group, count):
    for _ in range(count):
        enemy = Enemy()
        group.add(enemy)

# Основная функция игры
def game_loop():
    player = Player()
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    all_sprites.add(player)
    create_enemies(enemies, 5)
    all_sprites.add(enemies)

    clock = pygame.time.Clock()
    running = True

    while running:
        # Закрытие окна
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Обновление позиций игрока и врагов
        all_sprites.update()

        # Проверка на столкновение игрока с врагами
        if pygame.sprite.spritecollideany(player, enemies):
            print("Игра окончена!")
            running = False

        # Очистка экрана
        screen.fill(BLACK)

        # Отрисовка всех спрайтов
        all_sprites.draw(screen)

        # Обновление экрана
        pygame.display.flip()

        # Ограничение FPS
        clock.tick(60)

# Запуск игры
game_loop()
