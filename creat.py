import pygame
import vlc
import time

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
    text_rect = text_surf.get_rect(center=(button_surface.get_width() / 2 ,
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

def sprite(x:int, y:int, h:int, w:int, file_name:str, transform=False) -> pygame.Surface:
    """отрисовка справйтов и реогирование на нажатие

    Args:
        x (int): X координата
        y (int): y координата
        h (int): ширена
        w (int): высота
        file_name (str): имя картинки(путь да нее)
        transform (bool): будет ли изменяться разрешение обекта 

    Returns:
        _class_: Surface
    """
    img = pygame.image.load(file_name).convert_alpha()
    img_r = img.get_rect(bottomright=(x, y))
    if transform:
        img=pygame.transform.scale(img, (h, w)) # изменение размера
    #img.set_colorkey((255, 255, 255))
    CONSTANT.screen.blit(img, img_r)
    return img_r

def music(music_file:str, loop=-1):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(loops=loop)
    
def print_text(x:int, y:int, text:str, color=(0, 0, 0), font_size=28):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    CONSTANT.screen.blit(text_surface, (x,y))
    
    
def music_vlc(music_file:str, loop=1, volume=50):
    """запуск музыки

    Args:
        music_file (str): путь до файла
        loop (int, optional): соличество раз воспроизведения -1 бесконечное воспроизведения. Defaults to 1.
        volume (int, optional): громкость. Defaults to 50.
    """
    # Создаём инстанс VLC (без параметров окна)
    instance = vlc.Instance('--no-video', '--quiet')

    player = instance.media_player_new()
    media = instance.media_new(music_file)
    player.set_media(media)

    # Опционально: установить громкость (0-100)
    player.audio_set_volume(volume)

    player.play()

    while True:
        state = player.get_state()
        if state in (vlc.State.Ended, vlc.State.Stopped, vlc.State.Error):
            if loop>0 or loop==-1:
                player.stop()
                player.play()
                loop=loop-1
        time.sleep(0.2)