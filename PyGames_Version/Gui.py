import pygame
import pygame_gui
import threading

pygame.init()



pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((320, 240))

background = pygame.Surface((320, 240))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((320, 240))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 5), (50, 50)),
                                            text='Say Hello',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()