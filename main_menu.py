import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1280, 720))

def start_the_game():
    pass

menu = pygame_menu.Menu('Word Duelists', 1280, 720,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Singleplayer', start_the_game)
menu.add.button('Multiplayer', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)