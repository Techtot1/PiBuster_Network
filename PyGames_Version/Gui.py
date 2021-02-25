#!/usr/bin/python3
import pygame
import pygame_gui
import threading
import Networking
import adapter
import menu2

UI_e_folder = "UI_elements/"
UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"}
pygame.init()



# THE HOLY GRAIL. pygame_gui.core.ui_element.UIElement.hide(Iperf_Button)

Btn_size = (150,50)
cur_Ui = "Menu_1"


pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((320, 240))

background = pygame.Surface((320, 240))
background.fill(pygame.Color('#000000'))




manager = pygame_gui.UIManager((320, 240))

#
#
#
#
# MAIN MENU
Speedtest_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 0), Btn_size),
                                        text='Speedtest',
                                        manager=manager)

Iperf_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 75), Btn_size),
                                            text='Iperf',
                                            manager=manager)


Ping_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 150), Btn_size),
                                            text='Ping',
                                            manager=manager)

Next_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 190), (50,50)),
                                            text='>',
                                            manager=manager )





 

    #MENU2
    #
    #
    #
    #


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
                    if event.ui_element == Speedtest_Button:
                        print("This Is Speedtest")
                    if event.ui_element == Iperf_Button:
                        print("This Is Iperf")
                    if event.ui_element == Ping_Button:
                        print("This Is Ping")
                    if event.ui_element == Next_Button:
                        menu2.Gui()
        
    
    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    window_surface.blit(Connected, (0,205))

    manager.draw_ui(window_surface)

    pygame.display.update()