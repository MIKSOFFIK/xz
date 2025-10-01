import sys
import pygame


pygame.init()

clock = pygame.time.Clock()

# Создаём окно Pygame
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('FNae')

# Создаем объект шрифта
font = pygame.font.Font(None, 24)

# Создайте поверхность для кнопки
button_surface = pygame.Surface((150, 50))

# Отображение текста на кнопке
text = font.render("start", True, (0, 0, 0))
text_rect = text.get_rect(
    center=(button_surface.get_width() /2, 
            button_surface.get_height()/2))

# Создайте объект pygame.Rect, который представляет границы кнопки
button_rect = pygame.Rect(125, 125, 150, 50)  # Отрегулируйте положение

while True:
    clock.tick(60)
    screen.fill((155, 255, 155))

    # Получаем события из очереди событий
    for event in pygame.event.get():
        # Проверьте событие выхода
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Проверяем событие нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Вызовите функцию on_mouse_button_down()
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")

    # Проверьте, находится ли мышь над кнопкой. 
    # Это создаст эффект наведения кнопки.
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
 
    # Показать текст кнопки
    button_surface.blit(text, text_rect)

    # Нарисуйте кнопку на экране
    screen.blit(button_surface, (button_rect.x, button_rect.y))

    # Обновить состояние
    pygame.display.update()