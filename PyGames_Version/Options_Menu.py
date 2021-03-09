

import pygame
import pygame_gui
import threading
import os
import Networking
import adapter
import json
def Gui():
    
    pygame.init()
    pygame.display.set_caption('Options')
    window_surface = pygame.display.set_mode((320, 240))
    Btn_size = (150,50)
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color("#a493bf"))
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if event.type == pygame.QUIT:
                is_running = False
            manager.process_events(event)     
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == But1:
                        print("This Is Display ")
                    if event.ui_element == But2:
                        print("This Is Interface")
                        interface()                        
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
    pygame.display.set_caption('Inter Faces')
    window_surface = pygame.display.set_mode((320, 240))
    Btn_size = (150,50)
    UI_e_folder = "UI_elements/"
    UI_elements = {"connected":f"{UI_e_folder}Connected_dark.png","disconnected":f"{UI_e_folder}Disconnected_dark.png"} 
    background = pygame.Surface((320, 240))
    background.fill(pygame.Color("#b593bf"))
    
    
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
            elif interfaces.index(i)>3 and interfaces.index(i)<=6:
                locals()[i+"But"]  = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((160, 50*(interfaces.index(i)-4)), Btn_size),
                                                text=i+oof,
                                                manager=manager,object_id=pygame_gui.core.ObjectID(f"color-button-{i}") )           
    Prev_Button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((220, 190), (50,50)),
                                        text='<',
                                        manager=manager )
    Reset = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((170,190),(50,50)),
                                                text="Reset", manager=manager)
    off_ = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270,190),(50,50)),text="off",manager=manager)

    clock = pygame.time.Clock()
    is_running = True
    for i in interfaces:
        locals()[f"{i}But"].colours["normal_text"] = pygame.Color(26, 25, 28) 
        locals()[f"{i}But"].rebuild()     


    with open(os.getcwd()+"/Interfaces.json","r+") as Adapters_status_get:
        Adapters_status = json.load(Adapters_status_get)
    
    for i in interfaces:
        status = Adapters_status[i]
        if status == True:
            locals()[f"{i}But"].colours["normal_bg"] = pygame.Color(120, 204, 126) 
            locals()[f"{i}But"].rebuild()
            print("green")
            continue
        elif status == False:
            locals()[f"{i}But"].colours["normal_bg"] = pygame.Color(224, 99, 99) 
            locals()[f"{i}But"].rebuild()   
            print("red")     
    def colour_update(obj,col):
        obj.colours["normal_bg"] = pygame.Color((col)) 
        obj.rebuild()     
        print()

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
                    if event.ui_element == Prev_Button:
                        
                        return()
                    if event.ui_element == Reset:
                        adapter.adapter_reset()
                        for i in interfaces:
                            status_adap = adapter.get_cur_status(i)
                            if status_adap == True:
                            
                                colour_update(locals()[f"{i}But"],(120,204,126))
                            else:
                                
                                colour_update(locals()[f"{i}But"],(224, 99, 99))
                    if event.ui_element == off_:
                        for i in interfaces:
                            adapter.adapter_stop(i)
                            colour_update(locals()[f"{i}But"],(224, 99, 99))
                          
                    
                    for i in interfaces:
                        if event.ui_element == locals()[i+"But"]:
                            status = adapter.toggle(i)

                            if status == True:
                                locals()[f"{i}But"].colours["normal_bg"] = pygame.Color(120, 204, 126) 
                                locals()[f"{i}But"].rebuild()
                                print("green")
                                for ii in interfaces:
                                    if ii != i:
                                        adapter.adapter_stop(ii)
                                        locals()[f"{ii}But"].colours["normal_bg"] = pygame.Color(224, 99, 99) 
                                        locals()[f"{ii}But"].rebuild()   
                                        print("red")  
                            elif status == False:
                                locals()[f"{i}But"].colours["normal_bg"] = pygame.Color(224, 99, 99) 
                                locals()[f"{i}But"].rebuild()   
                                print("red")                         
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        window_surface.blit(Connected, (0,205))
        

        manager.draw_ui(window_surface)
        pygame.display.update()

#Gui()