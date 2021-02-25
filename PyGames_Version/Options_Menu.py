

import pygame
import pygame_gui
import threading

import Networking
import adapter

def Gui():
    
    pygame.init()
    pygame.display.set_caption('Sub Menu')
    window_surface = pygame.display.set_mode((320, 240))
    Btn_size = (150,50)
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color("#344185"))
    manager = pygame_gui.UIManager((320, 240))
  

    clock = pygame.time.Clock()
    is_running = True


    But1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 0), Btn_size),
                                    text='Display',
                                    manager=manager)

    But2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 75), Btn_size),
                                            text='Interfaces',
                                            manager=manager)
 
    But3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 150), Btn_size),
                                            text='N/a',
                                            manager=manager)
   
    Prev_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((220, 190), (50,50)),
                                            text='<',
                                            manager=manager )
                                        

                           
                    
    
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
                    if event.ui_element == But1:
                        print("This Is Display ")
                    if event.ui_element == But2:
                        print("This Is Interface")                        
                    if event.ui_element == But3:
                        print("N/A")
                    if event.ui_element == Prev_Button:
                        return None 
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))
        manager.draw_ui(window_surface)
        pygame.display.update()








def interface():
    interfaces = adapter.Adapters()
    pygame.init()
    pygame.display.set_caption('Sub Menu')
    window_surface = pygame.display.set_mode((320, 240))
    Btn_size = (150,50)
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color("#344185"))
    
    thing = pygame.Surface((0, 50)).fill(pygame.Color("#00ff00"))
    manager = pygame_gui.UIManager((320, 240),"theme.json")
    oof = "   s"
    if len(interfaces)<=4:
        for i in interfaces:
           locals()[i+"But"]  = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 50*interfaces.index(i)), Btn_size),
                                            text=i,
                                            manager=manager)
    elif len(interfaces)<=8:
        for i in interfaces:
            if interfaces.index(i)<=3:
                print(i)
                locals()[i+"But"]  = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 50*interfaces.index(i)), Btn_size),
                                                text=i+oof,
                                                manager=manager)
            elif interfaces.index(i)>3 and interfaces.index(i)<=7:
                locals()[i+"But"]  = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((160, 50*(interfaces.index(i)-4)), Btn_size),
                                                text=i+oof,
                                                manager=manager,object_id=pygame_gui.core.ObjectID(f"color-button-{i}") )           
    
    clock = pygame.time.Clock()
    is_running = True
    
    print(len(interfaces))


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
                    for i in interfaces:
                        if event.ui_element == locals()[i+"But"]:
                            
                            print(locals()[f"{i}But"].colours)
                            locals()[f"{i}But"].colours["normal_bg"] = pygame.Color(0, 98, 255) 
                            locals()[f"{i}But"].rebuild()

        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))
        

        manager.draw_ui(window_surface)
        pygame.display.update()

interface()