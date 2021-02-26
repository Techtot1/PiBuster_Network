

import pygame
import pygame_gui
import threading

import Networking
import adapter
import Options_Menu 
import time

def Download():
    pygame.init()
    pygame.display.set_caption('Menu 2')
    window_surface = pygame.display.set_mode((320, 240))
    
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color(11,12,27))
    manager = pygame_gui.UIManager((320, 240))
    
    
    
    Speedtest_Download = threading.Thread(target=Networking.speedtest_download)
    Speedtest_Download.start()
    font = pygame.font.SysFont(None, 25)
   

    
    Prev_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((220, 190), (50,50)),
                                            text='<',
                                            manager=manager)       

    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        print(pygame.time.get_ticks())
        text_img = 'sd'
        pygame.time.set_timer("")
        img = font.render(text_img, True, pygame.Color(28,191,255))

        
        Connected = pygame.image.load(UI_elements[adapter.connection()])
        Connected = pygame.transform.scale(Connected, (int(320/3), int(90/3)))
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if event.type == pygame.QUIT:
                is_running = False
            manager.process_events(event)     
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Prev_Button:
                        return None 
        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))
        window_surface.blit(img, (20, 20))

        manager.draw_ui(window_surface)
        pygame.display.update()
def Gui():
    
    pygame.init()
    pygame.display.set_caption('Menu 2')
    window_surface = pygame.display.set_mode((320, 240))
    Btn_size = (150,50)
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color(11,12,27))
    manager = pygame_gui.UIManager((320, 240))
       

    clock = pygame.time.Clock()
    is_running = True


    But1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 0), Btn_size),
                                    text='Download',
                                    manager=manager)

    But2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 75), Btn_size),
                                            text='Upload',
                                            manager=manager)


    But3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 150), Btn_size),
                                            text='Ping',
                                            manager=manager)
    Prev_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((220, 190), (50,50)),
                                            text='<',
                                            manager=manager)
    Buttons = (But1,But2,But3)
    for i in Buttons:                                        
        i.colours["normal_border"] = pygame.Color(28,191,255)
        i.colours["normal_text"] = pygame.Color(28,191, 255 )                                        
        i.rebuild()
                           

    while is_running:
        Connected = pygame.image.load(UI_elements[adapter.connection()])
        Connected = pygame.transform.scale(Connected, (int(320/3), int(90/3)))
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if event.type == pygame.QUIT:
                is_running = False
            manager.process_events(event)     
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == But1:
                        print("This Is IP Check")
                    if event.ui_element == But2:
                        print("This Is options")                        
                    if event.ui_element == But3:
                        print("N/A")
                    if event.ui_element == Prev_Button:
                        return None 
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))
        manager.draw_ui(window_surface)
        pygame.display.update()




Download()
#Gui()