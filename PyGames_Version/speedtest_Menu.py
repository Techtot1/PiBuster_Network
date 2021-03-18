

import pygame
import pygame_gui
import threading
import Networking
import adapter

import Options_Menu 
import time
import os 
import concurrent.futures
os.environ["SDL_FBDEV"] = "/dev/fb1"

    
def Download(g):
    os.environ["SDL_FBDEV"] = "/dev/fb1"

    pygame.init()
    pygame.display.set_caption('Menu 2')
    window_surface = pygame.display.set_mode((320, 240))
    
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color(11,12,27))
    manager = pygame_gui.UIManager((320, 240))
    
    speed_text_block_2 = pygame_gui.elements.UITextBox(f'<font face=fira_code size=4 color= #ffffff>SpeedTest Is running...<b></b>',
                             pygame.Rect((0, 0), (230, 50)),
                             manager=manager)
    speed_text_block_2.set_active_effect('fade_in')



    Prev_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((220, 190), (50,50)),
                                            text='<',
                                            manager=manager)
    restart_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((120,190),(100,50)), text="restart",manager=manager)                                              

    clock = pygame.time.Clock()
    is_running = True
    test_running = False
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
                    if event.ui_element == Prev_Button:
                        return None 
                    if event.ui_element == restart_button:
                        download = 0
                        test_running = False
                        speed_text_block_2 = pygame_gui.elements.UITextBox(f'<font face=fira_code size=4 color= #ffffff>SpeedTest Is running...<b></b>',
                                pygame.Rect((0, 0), (230, 50)),
                                manager=manager)
                        speed_text_block_2.set_active_effect('fade_in')
            
                    
        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))
       # window_surface.blit(img, (20, 20))

        manager.draw_ui(window_surface)
        pygame.display.update()
        if not test_running and g == True :
            download = Networking.speedtest_download()
            test_running = True
        if download > 0:
            speed_text_block_2 = pygame_gui.elements.UITextBox(f'<font face=fira_code size=4 color= #ffffff>download: {download} mbps<b></b>',
                             pygame.Rect((0, 0), (230, 50)),
                             manager=manager)
            speed_text_block_2.set_active_effect('fade_in')
         
def Upload(g):
    os.environ["SDL_FBDEV"] = "/dev/fb1"

    pygame.init()
    pygame.display.set_caption('Menu 2')
    window_surface = pygame.display.set_mode((320, 240))
    
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color(11,12,27))
    manager = pygame_gui.UIManager((320, 240))
    
    speed_text_block_2 = pygame_gui.elements.UITextBox(f'<font face=fira_code size=4 color= #ffffff>SpeedTest Is running...<b></b>',
                             pygame.Rect((0, 0), (230, 50)),
                             manager=manager)
    speed_text_block_2.set_active_effect('fade_in')



    Prev_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((220, 190), (50,50)),
                                            text='<',
                                            manager=manager)
    restart_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((120,190),(100,50)), text="restart",manager=manager)                                              

    clock = pygame.time.Clock()
    is_running = True
    test_running = False
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
                    if event.ui_element == Prev_Button:
                        return None 
                    if event.ui_element == restart_button:
                        upload = 0
                        test_running = False
                        speed_text_block_2 = pygame_gui.elements.UITextBox(f'<font face=fira_code size=4 color= #ffffff>SpeedTest Is running...<b></b>',
                                pygame.Rect((0, 0), (230, 50)),
                                manager=manager)
                        speed_text_block_2.set_active_effect('fade_in')
            
                    
        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))
       # window_surface.blit(img, (20, 20))

        manager.draw_ui(window_surface)
        pygame.display.update()
        if not test_running and g==True:
            upload = Networking.speedtest_upload()
            test_running = True 
        if upload > 0:
            speed_text_block_2 = pygame_gui.elements.UITextBox(f'<font face=fira_code size=4 color= #ffffff>Upload: {upload} mbps<b></b>',
                             pygame.Rect((0, 0), (230, 50)),
                             manager=manager)
            speed_text_block_2.set_active_effect('fade_in')
         
def ping(g):
    os.environ["SDL_FBDEV"] = "/dev/fb1"

    pygame.init()
    pygame.display.set_caption('Menu 2')
    window_surface = pygame.display.set_mode((320, 240))
    
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color(11,12,27))
    manager = pygame_gui.UIManager((320, 240))
    
    speed_text_block_2 = pygame_gui.elements.UITextBox(f'<font face=fira_code size=4 color= #ffffff>SpeedTest Is running...<b></b>',
                             pygame.Rect((0, 0), (230, 50)),
                             manager=manager)
    speed_text_block_2.set_active_effect('fade_in')



    Prev_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((220, 190), (50,50)),
                                            text='<',
                                            manager=manager)
    restart_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((120,190),(100,50)), text="restart",manager=manager)                                              

    clock = pygame.time.Clock()
    is_running = True
    test_running = False
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
                    if event.ui_element == Prev_Button:
                        return None 
                    if event.ui_element == restart_button:
                        ping = 0
                        test_running = False
                        speed_text_block_2 = pygame_gui.elements.UITextBox(f'<font face=fira_code size=4 color= #ffffff>SpeedTest Is running...<b></b>',
                                pygame.Rect((0, 0), (230, 50)),
                                manager=manager)
                        speed_text_block_2.set_active_effect('fade_in')
            
                    
        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))
       # window_surface.blit(img, (20, 20))

        manager.draw_ui(window_surface)
        pygame.display.update()
        if not test_running and g==True:
            ping = Networking.speedtest_latency()
            test_running = True 
        if upload > 0:
            speed_text_block_2 = pygame_gui.elements.UITextBox(f'<font face=fira_code size=4 color= #ffffff>Upload: {upload} mbps<b></b>',
                             pygame.Rect((0, 0), (230, 50)),
                             manager=manager)
            speed_text_block_2.set_active_effect('fade_in')
      

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


    But1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 0), Btn_size),
                                    text='Download',
                                    manager=manager)

    But2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 75), Btn_size),
                                            text='Upload',
                                            manager=manager)


    But3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 150), Btn_size),
                                            text='Ping',
                                            manager=manager)
    But4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((165, 0), Btn_size),
                                        text='Up & Down',
                                        manager=manager)
    Prev_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((220, 190), (50,50)),
                                            text='<',
                                            manager=manager)
    Buttons = (But1,But2,But3,But4)
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
                        Download(True)
                    if event.ui_element == But2:
                        Upload(True)                        
                    if event.ui_element == But3:
                        ping(True)
                    if event.ui_element == Prev_Button:
                        return None 
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))
        manager.draw_ui(window_surface)
        pygame.display.update()




#Download()
Gui()



def test_gui():
    pygame.init()
    pygame.display.set_caption('Menu 2')
    window_surface = pygame.display.set_mode((320, 240))
    Btn_size = (150,50)
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color(11,12,27))
    manager = pygame_gui.UIManager((320, 240))
    is_running = True
    htm_text_block_2 = pygame_gui.elements.UITextBox('<font face=fira_code size=4 color=#ffffff><b>Hey, What the heck!</b>',
                             pygame.Rect((0, 0), (200, 150)),
                             manager=manager)
    htm_text_block_2.set_active_effect('fade_in')
    clock = pygame.time.Clock()
    while is_running:
        Connected = pygame.image.load(UI_elements[adapter.connection()])
        Connected = pygame.transform.scale(Connected, (int(320/3), int(90/3)))
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return()
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))
        manager.draw_ui(window_surface)
        pygame.display.update()
#test_gui()