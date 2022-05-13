import pygame
import pygame_menu
import sys
import os

pygame.init()
surface = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
clock.tick(60)
def singleplayer():
    pygame.quit()
    os.system('singleplayer.py')
    pygame.display.set_caption("Singleplayer")
    r=True
    while r==True:
        surface.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                r=False
        pygame.display.update()

def multiplayer():
    pygame.quit()
    os.system('multiplayer.py')
    pygame.display.set_caption("Multiplayer")
    r=True
    while r==True:
        surface.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                r=False
        pygame.display.update()

def howtoplay():
    os.system('howtoplay.py')
    pygame.display.set_caption("HowToPlay")
    r=True
    while r==True:
        surface.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                r=False
                os.system('main_menu.py')
                sys.exit()
        pygame.quit()
        os.system('main_menu.py')
        pygame.display.update()



menu = pygame_menu.Menu('Word Duelists', 1280, 720,theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Singleplayer', singleplayer)
menu.add.button('Multiplayer', multiplayer)
menu.add.button('How To Play', howtoplay)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)