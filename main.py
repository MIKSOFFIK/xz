import sys
import random
import os
import threading
import time
import pygame

from creat import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Окно
window_size = (1100, 800)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('FNaE')

# Шрифт (текст не отрисовывается по требованию, но шрифт оставлен если понадобится)
font = pygame.font.Font(None, 24)

CONSTANT.font = font
CONSTANT.screen = screen

menu=True # указывает на то что игрок в меню
plauing=False # указывает на то что игрок играет
open_camera=False # указывает на то отрыты ли камеры или нет

'''
#отладочнный режим
menu=False 
plauing=True 
open_camera=True 
'''

number_camera = 1


position={
    "holl": ["hitler", None],
    "coredor": [None, None],
    "zal": ["egor", None],
    "toilet": [None, None]
}
shkatulka=0 # шкатулка гитлера от 0 до 30 

def main():
    global menu, plauing, open_camera, number_camera, gitler_logic
    
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
                
                hourus=12
                minute=00
                print_text(dis_w-30, dis_h-30, f"{hourus}:{minute}")
                
                open_camera_button = sprite(dis_w-0, dis_h-170, 150,200, os.path.join(os.getcwd(), "asets", "open_camera.png"))
                if open_camera_button.collidepoint(clic_event):

                    if open_camera:
                        open_camera = False
                        print("close_camera")    
                        music(os.path.join(os.getcwd(), "asets", "sount", "blip.mp3"), 0)
                    else:
                        open_camera = True
                        print("open_camera")
                        music(os.path.join(os.getcwd(), "asets", "sount", "blip.mp3"), 0)
                    
                if open_camera: # тут логика камеры
                    sprite(dis_w-100, dis_h-200, 700,500, os.path.join(os.getcwd(), "asets", "plonshet.png"))
                    #создание кнопок камеры
                    button1 = sprite(dis_w - 220, dis_h- 420, 30, 30, os.path.join(os.getcwd(), "asets", "camers", "cam_button", "1.png"))
                    button2 = sprite(dis_w - 220, dis_h- 320, 30, 30, os.path.join(os.getcwd(), "asets", "camers", "cam_button", "2.png"))
                    button3 = sprite(dis_w - 200, dis_h- 470, 30, 30, os.path.join(os.getcwd(), "asets", "camers", "cam_button", "3.png"))
                    button4 = sprite(dis_w - 150, dis_h- 260, 30, 30, os.path.join(os.getcwd(), "asets", "camers", "cam_button", "4.png"))
                    button5 = sprite(dis_w - 240, dis_h- 390, 30, 30, os.path.join(os.getcwd(), "asets", "camers", "cam_button", "4.png"))
                    # переключения между камерами
                    if button1.collidepoint(clic_event) and number_camera != 1:
                        number_camera = 1
                        music(os.path.join(os.getcwd(), "asets", "sount", "clic_camers.mp3"), 0)
                        print("cam 1")
                    if button2.collidepoint(clic_event) and number_camera != 2:
                        number_camera = 2
                        music(os.path.join(os.getcwd(), "asets", "sount", "clic_camers.mp3"), 0)
                        print("cam 2")
                    if button3.collidepoint(clic_event) and number_camera != 4:
                        number_camera = 3
                        music(os.path.join(os.getcwd(), "asets", "sount", "clic_camers.mp3"), 0)
                        print("cam 3")
                    if button4.collidepoint(clic_event) and number_camera != 3:
                        number_camera = 4
                        music(os.path.join(os.getcwd(), "asets", "sount", "clic_camers.mp3"), 0)
                        print("cam 4")
                    if button5.collidepoint(clic_event) and number_camera != 4:
                        number_camera = 5
                        music(os.path.join(os.getcwd(), "asets", "sount", "clic_camers.mp3"), 0)
                        print("cam 5")

                    if number_camera == 1:
                        sprite(dis_w-340, dis_h-271, 400, 390, os.path.join(os.getcwd(), "asets", "camers", "toalets.jpg"))
                    if number_camera == 2:
                        sprite(dis_w-340, dis_h-271, 400, 390, os.path.join(os.getcwd(), "asets", "camers", "holl.jpg"))
                    if number_camera == 3:
                        if position["holl"][0]=="hitler":
                            sprite(dis_w-340, dis_h-271, 400, 390, os.path.join(os.getcwd(), "asets", "camers", "gitler.jpg"))
                        else:
                            sprite(dis_w-340, dis_h-271, 400, 390, os.path.join(os.getcwd(), "asets", "camers", "gitler_scena.jpg"))
                    if number_camera == 4:
                        sprite(dis_w-340, dis_h-271, 400, 390, os.path.join(os.getcwd(), "asets", "camers", "coredor.jpg"))

                else:
                    pass
                    
        pygame.display.update()
        
        

if __name__ == "__main__":
    # запускаю музыку и игру в разных потоках
    thread = threading.Thread(target=music(os.path.join(os.getcwd(), "asets", "sount", ["menu_embiend_2.mp3", "menu_embiendF.mp3"][random.randint(0,1)] )), daemon=True)  
    mainf = threading.Thread(main(), daemon=True)
    mainf.start()
    thread.start()

