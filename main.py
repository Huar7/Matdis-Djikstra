import pygame as pg
import pygame_gui as pgui
import os
from djikstra import *

def main(): ## func Ready
    pg.init()
    screen = pg.display.set_mode((1280, 720))
    clock = pg.time.Clock()
    running = True

    camera_offset_x = 0

    now = False
    mouse_current_pos = (0, 0)
    while running: ## Func Loop ==== ==== ====

        mouse_pos = pg.mouse.get_pos()
        
        ## Event Loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN: ## untuk mouse
                if event.button == 2:
                    mouse_current_pos = mouse_pos ## untuk mengset posisi ketika di pencet
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 2:
                    pass ## ini ketika mouse dilepas

            if event.type == pg.KEYDOWN: ## untuk kunci yang dipencet
                if event.key == pg.K_1:
                    now = True
            if event.type == pg.KEYUP: ## untuk kunci yang dilepas
                 if event.key == pg.K_1:
                    now = False
               


        # fill the screen with a color to wipe away anything from last frame
        screen.fill("grey")

        if now:
            print(mouse_pos[0] - mouse_current_pos[0])
            #print(mouse_pos[1] - mouse_current_pos[1])


        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pg.display.flip()

        clock.tick(60)  # limits FPS to 60

    pg.quit()
    os.system('cls' if os.name == 'nt' else 'clear') ## membersihkan Debugger Terminal

if __name__ == '__main__':
    main()
