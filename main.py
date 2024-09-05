import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Пинг-Понг')

# Определение цветов
WHITE = (255, 255, 255)

# Определение размеров ракеток и мяча
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
BALL_SIZE = 15

# Скорости
PADDLE_SPEED = 7
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Начальные позиции ракеток и мяча
left_paddle = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
                           PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Начальные скорости мяча
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Начальные очки
left_score = 0
right_score = 0

# Шрифт для отображения счета
font = pygame.font.Font(None, 74)

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Получение нажатий клавиш
    keys = pygame.key.get_pressed()

    # Управление левой ракеткой
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
        left_paddle.y += PADDLE_SPEED

    # Управление правой ракеткой
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Перемещение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Проверка столкновений мяча с верхней и нижней границами
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y

    # Проверка столкновений мяча с ракетками
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x = -ball_speed_x

    # Проверка на то, что мяч вышел за пределы экрана
    if ball.left <= 0:
        right_score += 1
        ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE,
                           BALL_SIZE)
        ball_speed_x = BALL_SPEED_X
        ball_speed_y = BALL_SPEED_Y
    if ball.right >= SCREEN_WIDTH:
        left_score += 1
        ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE,
                           BALL_SIZE)
        ball_speed_x = -BALL_SPEED_X
        ball_speed_y = BALL_SPEED_Y

    # Очистка экрана
    screen.fill(SCREEN_COLOR)

    # Отрисовка объектов
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Отображение счета
    left_text = font.render(str(left_score), True, WHITE)
    screen.blit(left_text, (SCREEN_WIDTH // 2 - 50, 10))
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(right_text, (SCREEN_WIDTH // 2 + 25, 10))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    pygame.time.Clock().tick(60)
