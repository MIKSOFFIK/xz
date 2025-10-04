import sys
import random
import os
import threading 

import pygame

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Окно
window_size = (1100, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('FNaE')

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
    screen.blit(img, img_r)
    return img_r

def music(music_file:str, loop=-1):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(loops=loop)

menu=True #указывает на то что игрок в меню 
plauing=False #указвыает на то что игрок играет
open_camera=False # указывает на то отрыты ли камеры или нет

number_camera = 1

def main():
    global menu, plauing, open_camera, number_camera
    while True:
        clock.tick(60)
        dis_w, dis_h = pygame.display.get_surface().get_size()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:# открытие меню по нажатию на esc
                    menu=True 
                    plauing=False
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:# это костыль за за которого теперь нельзя выставлять кнопки на координаты 0.0 0.0
                clic_event=event.pos
            else:
                clic_event=0.0,0.0
                
            if menu:
                screen.fill((36, 36, 36))  # фон окна
                poshalco = sprite(dis_w,dis_h,200,150, os.path.join(os.getcwd(), "asets", "egorka.png"))
                
                exit_button = creat_button(10, 700, 100, 75, "Exit") # создание кнопки
                start_button = creat_button(10, 628, 100, 75, "Start")
                if exit_button.collidepoint(clic_event):
                    print("exit")
                    pygame.quit()
                    sys.exit()
                    
                if start_button.collidepoint(clic_event):
                    menu=False #отключаем меню
                    plauing=True #включаем игру
                    print("start")   
                    
                if poshalco.collidepoint(clic_event):
                    print("пасхлка")# доделать
                
            if plauing:
                #фон
                img = pygame.image.load(os.path.join(os.getcwd(), "asets", "offise.jpg")).convert_alpha()
                img = pygame.transform.scale(img, (dis_w, dis_h))# растягиваю на весь экран
                screen.blit(img, (0,0))
                
                open_camera_button = sprite(dis_w-300, dis_h-10, 150,200, os.path.join(os.getcwd(), "asets", "open_camera.png"))
                if open_camera_button.collidepoint(clic_event):

                    if open_camera:
                        open_camera = False
                        print("close_camera")    
                    else:
                        open_camera = True
                        print("open_camera")
                        music(os.path.join(os.getcwd(), "asets", "sount", "blip.mp3"), 0)
                    
                    
                if open_camera: # тут логика камеры
                    sprite(dis_w-30, dis_h-200, 700,500, os.path.join(os.getcwd(), "asets", "plonshet.png"))
                    #создание кнопок камеры
                    button1 = sprite(dis_w - 185, dis_h- 350, 30, 30, os.path.join(os.getcwd(), "asets", "camers", "cam_button", "1.png"))
                    button2 = sprite(dis_w - 150, dis_h- 320, 30, 30, os.path.join(os.getcwd(), "asets", "camers", "cam_button", "2.png"))
                    button3 = sprite(dis_w - 86, dis_h- 260, 30, 30, os.path.join(os.getcwd(), "asets", "camers", "cam_button", "3.png"))
                    button4 = sprite(dis_w - 135, dis_h- 470, 30, 30, os.path.join(os.getcwd(), "asets", "camers", "cam_button", "4.png"))
                    # переключения между камерами
                    if button1.collidepoint(clic_event) and number_camera != 1:
                        number_camera = 1
                        music(os.path.join(os.getcwd(), "asets", "sount", "blip.mp3"), 0)
                        print("cam 1")
                    if button2.collidepoint(clic_event) and number_camera != 2:
                        number_camera = 2
                        music(os.path.join(os.getcwd(), "asets", "sount", "blip.mp3"), 0)
                        print("cam 2")
                    if button3.collidepoint(clic_event) and number_camera != 3:
                        number_camera = 3
                        music(os.path.join(os.getcwd(), "asets", "sount", "blip.mp3"), 0)
                        print("cam 3")
                    if button4.collidepoint(clic_event) and number_camera != 4:
                        number_camera = 4
                        music(os.path.join(os.getcwd(), "asets", "sount", "blip.mp3"), 0)
                        print("cam 4")

                    if number_camera == 1:
                        sprite(dis_w-270, dis_h-271, 400, 390, os.path.join(os.getcwd(), "asets", "camers", "toalets.jpg"))
                    if number_camera == 2:
                        sprite(dis_w-270, dis_h-271, 400, 390, os.path.join(os.getcwd(), "asets", "camers", "holl.jpg"))
                    if number_camera == 3:
                        sprite(dis_w-270, dis_h-271, 400, 390, os.path.join(os.getcwd(), "asets", "camers", "coredor.jpg"))
                    if number_camera == 4:
                        sprite(dis_w-270, dis_h-271, 400, 390, os.path.join(os.getcwd(), "asets", "camers", "gitler.jpg"))

                    
                else:
                    pass
                    
        pygame.display.update()
        
        

if __name__ == "__main__":
    # запускаю музыку и игру в разных потоках
    thread = threading.Thread(target=music(os.path.join(os.getcwd(), "asets", "sount", ["menu_embiend_2.mp3", "menu_embiendF.mp3"][random.randint(0,1)] )), daemon=True)  
    mainf = threading.Thread(main(), daemon=True)
    mainf.start()
    thread.start()
