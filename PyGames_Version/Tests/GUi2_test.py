

import pygame
import pygame_gui
import threading
import Networking
import adapter

def Gui_2():
    
    pygame.init()
    pygame.display.set_caption('Sub Menu')
    window_surface = pygame.display.set_mode((320, 240))
    Btn_size = (150,50)
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color("#344185"))
    manager = pygame_gui.UIManager((320, 240))


    Speedtest_Button_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 0), Btn_size),
                                            text='asd',
                                            manager=manager)
    clock = pygame.time.Clock()
    is_running = True

    while is_running:

        Connected = pygame.image.load(UI_elements[adapter.connection()])
        Connected = pygame.transform.scale(Connected, (int(320/3), int(90/3)))
        



        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Speedtest_Button_2:
                        return
                
        
        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))

        manager.draw_ui(window_surface)

        pygame.display.update()
