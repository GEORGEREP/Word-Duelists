import pygame
import pygame_menu
import os

pygame.init()
surface = pygame.display.set_mode((1280, 720))
def singleplayer():
    pygame.quit()
    os.system('main.py')
    pygame.display.set_caption("Singleplayer")
    r=True
    while r==True:
        surface.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                r=False
        pygame.display.update()
def start_the_game():
    pass

menu = pygame_menu.Menu('Word Duelists', 1280, 720,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Singleplayer', singleplayer)
menu.add.button('Multiplayer', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)