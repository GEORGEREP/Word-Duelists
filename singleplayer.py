import pygame
import sys
import random
from words import *

pygame.init()
clock = pygame.time.Clock()
clock.tick(60)

WIDTH, HEIGHT = 633, 900

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("assets/Grid.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 300))
ICON = pygame.image.load("assets/Icon.png")

pygame.display.set_caption("Word Duelists")
pygame.display.set_icon(ICON)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

CORRECT_WORD = (random.choice(WORDS))
print (CORRECT_WORD)
ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)

SCREEN.fill("black")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)

pygame.display.update()
LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75

guesses_count = 0

# Λίστα με τις προσπάθειες
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110

# Το indicator είναι υπεύθυνο για την λειτουργία των γραμμάτων κάτω απο το grid.
indicators = []

game_result = ""

class Letter:
    def __init__(self, text, bg_position):
        # Αρχικοποίηση των μεταβλητών όπως τα χρώματα, η γραμματοσειρά οι θέσεις και το μέγεθος.
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x+36, self.bg_position[1]+34)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        # Τοποθέτηση των γραμμάτων στις σωστές θέσεις.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self):
        # Άδειασμα των τετραγώνων.
        pygame.draw.rect(SCREEN, "black", self.bg_rect)
        pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3)
        pygame.display.update()

class Indicator:
    def __init__(self, x, y, letter):
        # Αρχικοποίηση μεταβλητών.
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 75)
        self.bg_color = OUTLINE

    def draw(self):
        # Τοποθέτηση των γραμμάτων κάτω από το grid.
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "black")
        self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+30))
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()

# Εμφάνιση των γραμμάτων κάτω απο το grid στην οθόνη.

indicator_x, indicator_y = 20, 600
indicator_x2, indicator_y2 = 770, 600

for i in range(3):
    for letter in ALPHABET[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 60
    indicator_y += 100
    if i == 0:
        indicator_x = 50
    elif i == 1:
        indicator_x = 105

def check_guess(guess_to_check):
    # Ελέγχει κάθε γράμμα και το σημειώνει ή πράσινο ή κίτρινο ή γκρι.
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result, LETTER_Y_SPACING
    game_decided = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
        if lowercase_letter in CORRECT_WORD:
            if lowercase_letter == CORRECT_WORD[i]:
                guess_to_check[i].bg_color = GREEN
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREEN
                        indicator.draw()
                guess_to_check[i].text_color = "black"
                if not game_decided:
                    game_result = "W"
            else:
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = YELLOW
                        indicator.draw()
                guess_to_check[i].text_color = "black"
                game_result = ""
                game_decided = True
        else:
            guess_to_check[i].bg_color = GREY
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = GREY
                    indicator.draw()
            guess_to_check[i].text_color = "black"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()
 
    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110

    if guesses_count == 6 and game_result == "":
        game_result = "L"

def play_again():
    # Εμφανίζεται το play again στην οθόνη.
    play_again_font = pygame.font.Font("assets/FreeSansBold.otf", 40)
    play_again_text = play_again_font.render("Press ENTER to Play Again", True, "white")
    play_again_rect = play_again_text.get_rect(center=(WIDTH/2.1, 300))
    word_was_text = play_again_font.render(f"The word was {CORRECT_WORD}", True, "white")
    word_was_rect = word_was_text.get_rect(center=(WIDTH/2.1, 150))
    SCREEN.blit(word_was_text, word_was_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()
def reset():
    # Επαναφορά των μεταβλητών στην αρχική τους κατάσταση.
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result, current_letter_bg_x, LETTER_Y_SPACING
    SCREEN.fill("black")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    guesses_count = 0
    CORRECT_WORD = random.choice(WORDS)
    print (CORRECT_WORD)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    current_letter_bg_x = 110

    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()

def create_new_letter():
    # Δημιουργεί και προσθέτει νέο γράμμα.
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count*100+LETTER_Y_SPACING))
    current_letter_bg_x += LETTER_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()

def delete_letter():
    # Διαγράφει το προηγούμενο γράμμα.
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING
while True:
    if game_result != "":
        play_again()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if game_result != "":
                    reset()
                else:
                    if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS:
                        check_guess(current_guess)
            elif event.key == pygame.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()