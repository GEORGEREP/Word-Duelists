import random, pygame, sys
from english_words import english_words_lower_alpha_set
from pygame.locals import *
pygame.init()

white = (255,255,255)
yellow = (255,255,102)
grey = (211, 211, 211)
black = (0,0,0)
green=(0,255,0)
lightGreen=(153,255,204)

font = pygame.font.SysFont("Helvetica neue", 40)
bigFont = pygame.font.SysFont("Helvetica neue", 80)

youWin = bigFont.render("You Win!",       True, lightGreen)
youLose = bigFont.render("You Lose!",     True, lightGreen)
playAgain = bigFont.render("Play Again?", True, lightGreen)

def checkGuess(turns, words, userGuess, window):
    renderList = ["","","","",""]
    spacing = 0
    guessColourCode = [grey,grey,grey,grey,grey]

    for i in range(0,5):
        if userGuess[i] in words:
            guessColourCode[i] = yellow

        if words[i] == userGuess[i]:
            guessColourCode[i] = green

    list(userGuess)

    for i in range(0,5):
        renderList[i] = font.render(userGuess[i], True, black)
        pygame.draw.rect(window, guessColourCode[i], pygame.Rect(60 +spacing, 50+ (turns*80), 50, 50))
        window.blit(renderList[i], (70 + spacing, 50 + (turns*80)))
        spacing+=80

    if guessColourCode == [green,green,green,green,green]:
        return True



def main():
    words=[]
    for i in english_words_lower_alpha_set:
        if len(i)==5:
            words.append(i)
    height = 600
    width = 500

    FPS = 30
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    window.fill(black)

    guess = ""

    for i in range(0,5):
        for j in range(0,5):
            pygame.draw.rect(window, grey, pygame.Rect(60+(i*80), 50+(j*80), 50, 50),2)

    pygame.display.set_caption("Word Duelists")

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.exit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                guess+=event.unicode.upper()

                if event.key == K_RETURN and win == True:
                    main()

                if event.key == K_RETURN and turns == 6:
                    main()

                if event.key == pygame.K_BACKSPACE or len(guess) > 5:
                    guess = guess[:-1]

                if event.key == K_RETURN and len(guess) > 4:
                    win = checkGuess(turns, words, guess, window)
                    turns+=1
                    guess = ""
                    window.fill(black,(0,500, 500, 200))

        window.fill(black,(0,500, 500, 200))
        renderGuess = font.render(guess, True, grey)
        window.blit(renderGuess, (180, 530))

        if win == True:
            window.blit(youWin,(90,200))
            window.blit(playAgain,(60,300))

        if turns == 6 and win != True:
            window.blit(youLose,(90,200))
            window.blit(playAgain,(60,300))
        pygame.display.update()
        clock.tick(FPS)
main()