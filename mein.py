import sys
import pygame

pygame.init()
clock = pygame.time.Clock()

# Окно
window_size = (700, 700)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('FNae')

# Шрифт (текст не отрисовывается по требованию, но шрифт оставлен если понадобится)
font = pygame.font.Font(None, 24)

def creat_button(x: int, y: int, h: int, w: int, text: str)-> pygame.Rect:
    """создание кнопок с текстом

    Args:
        x (int): X(left) координата
        y (int): y(top) координата
        h (int): ширена кнопки
        w (int): высота кнопки
        text (str): текст на кнопке

    Returns:
        _pygame.Rect_: класс кнопки
    """
    # Создаем поверхность для кнопки (без цветовой заливки кнопки)
    button_surface = pygame.Surface((h, w), pygame.SRCALPHA)  # поддержка прозрачности

    # Подготовка текста (не отрисовываем его на поверхности по вашему требованию)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=(button_surface.get_width() / 2,
                                           button_surface.get_height() / 2))

    # Рект кнопки (координаты на экране)
    button_rect = pygame.Rect(x, y, h, w)

    # Эффект наведения без изменения цвета: отрисуем тонкий контур при наведении
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (0, 0, 0, 50), button_surface.get_rect(), 2)  # полупрозрачный контур
    else:
        pygame.draw.rect(button_surface, (0, 0, 0, 0), button_surface.get_rect(), 1)  # невидимый/тонкий контур

    # По требованию: не выводим текст на кнопку
    button_surface.blit(text_surf, text_rect)

    # Рисуем кнопку на экране (поверх прозрачной поверхности будет виден фон окна)
    screen.blit(button_surface, (button_rect.x, button_rect.y))

    return button_rect

menu=True #указывает на то что игрок в меню 
plauing=False #указвыает на то что игрок играет

def main():
    global menu,plauing
    while True:
        clock.tick(60)
        screen.fill((36, 36, 36))  # фон окна

        if menu:
            exit_button = creat_button(10, 600, 100, 75, "Exit") # создание кнопки
            start_button = creat_button(10, 540, 100, 75, "Start")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if exit_button.collidepoint(event.pos):
                    print("exit")
                    pygame.quit()
                    sys.exit()
                if start_button.collidepoint(event.pos):
                    menu=False #отключаем меню
                    plauing=True #включаем игру
                    print("start")

        pygame.display.update()

if __name__ == "__main__":
    main()
