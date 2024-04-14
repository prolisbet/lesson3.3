import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('img/call-of-duty-mobile-003.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target2.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0
font = pygame.font.Font(None, 24)
background_color = (255, 255, 255)

text_background_width = 120
text_background_height = 25
text_background_x = 10
text_background_y = 10

loser_font = pygame.font.Font(None, 72)

loser_background_width = 360
loser_background_height = 200
loser_background_x = 220
loser_background_y = 200

running = True
game_over = False


def reset_game():
    global score, target_x, target_y, game_over, color
    score = 0
    game_over = False
    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


while running:
    screen.fill(color)

    text_background = pygame.Rect(text_background_x, text_background_y, text_background_width, text_background_height)
    pygame.draw.rect(screen, background_color, text_background)

    score_surface = font.render(f'Очки: {score}', True, (0, 0, 0))
    screen.blit(score_surface, [15, 15])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_r:
                reset_game()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (
                    target_x < mouse_x < target_x + target_width) and (
                    target_y < mouse_y < target_y + target_height):
                score += 10
            else:
                score -= 10
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    if not game_over:
        screen.blit(target_img, (target_x, target_y))
    else:
        loser_background = pygame.Rect(
            loser_background_x, loser_background_y, loser_background_width,
            loser_background_height)
        pygame.draw.rect(screen, background_color, loser_background)
        loser_surface = loser_font.render('YOU LOSE', True, (0, 0, 0))
        screen.blit(loser_surface, [270, 250])
        restart_surface = font.render('Нажмите R для перезапуска', True, (0, 0, 0))
        screen.blit(restart_surface, [280, 340])

    if score < 0:
        game_over = True

    pygame.display.update()


pygame.quit()