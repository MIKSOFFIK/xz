import pygame

class plauing_const():
    def __init__(self):
        self.font=pygame.font.Font
        self.screen=pygame.Surface
        
CONSTANT=plauing_const()


def creat_button(x: int, y: int, h: int, w: int, text: str, bord=0, text_color=(0, 0, 0))-> pygame.Rect:
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

    # Подготовка текста 
    text_surf = CONSTANT.font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=(button_surface.get_width() / 2,
                                           button_surface.get_height() / 2))

    # Рект кнопки (координаты на экране)
    button_rect = pygame.Rect(x, y, h, w, border_radius = bord)

    # Эффект наведения без изменения цвета: отрисуем тонкий контур при наведении
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (0, 0, 0, 50), button_surface.get_rect(), 2)  # полупрозрачный контур
    else:
        pygame.draw.rect(button_surface, (0, 0, 0, 0), button_surface.get_rect(), 1)  # невидимый/тонкий контур

    button_surface.blit(text_surf, text_rect)

    # Рисуем кнопку на экране (поверх прозрачной поверхности будет виден фон окна)
    CONSTANT.screen.blit(button_surface, (button_rect.x, button_rect.y))

    return button_rect

def sprite(x:int, y:int, h:int, w:int, file_name:str):
    """отрисовка справйтов и реогирование на нажатие

    Args:
        x (int): X координата
        y (int): y координата
        h (int): ширена
        w (int): высота
        file_name (str): имя картинки(путь да нее)

    Returns:
        _class_: Surface
    """
    img = pygame.image.load(file_name).convert_alpha()
    img_r = img.get_rect(bottomright=(x, y))
    #img.set_colorkey((255, 255, 255))
    CONSTANT.screen.blit(img, img_r)
    return img_r

def music(music_file:str, loop=-1):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(loops=loop)
    
def print_text(x:int, y:int, text:str ,color=(0, 0, 0)):
    text_surface = CONSTANT.font.render(text, True, color)
    CONSTANT.screen.blit(text_surface, (x,y))