import pygame

pygame.init()

WIDTH, HEIGHT = 600, 520

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("assets/instructions.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(300, 250))
ICON = pygame.image.load("assets/Icon.png")

pygame.display.set_caption("Word Duelists")
pygame.display.set_icon(ICON)

SCREEN.fill("black")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()