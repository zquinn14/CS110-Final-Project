import pygame, sys
import Controller
import random

"""Created by Megan and Hayden
Most everything in here coded by Megan,
Hayden contributed largely to the sound portion of the code and the game taunt"""

pygame.init()

#Display dimensions
display_w = 640
display_h = 480

"""Displays everything - Megan"""
screen = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption('Blockbusters')

clock = pygame.time.Clock()

#color options
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTRED = (250, 40, 10)
RED = (255, 0 , 0)
LIGHTGREEN = (50, 205, 50)
GREEN = (0, 100, 0)
YELLOW = (255, 165, 0)
LIGHTYELLOW = (255, 255, 0)
BLUE = (60, 179, 113)
PURPLE = (148, 0, 211)
GRAY = (139, 139, 131)

#font options
smallfont = pygame.font.SysFont('serif', 25, bold=True)
medsmfont = pygame.font.SysFont('serif', 34, bold=True)
mediumfont = pygame.font.SysFont('serif', 40, bold=True)
largefont = pygame.font.SysFont('serif', 70, bold=True)

"""Makes text object to display on a screen - Megan"""
def text_objects(text, color, size):
    #called by message_to_screen, needed to write the text
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medsm":
        textSurface = medsmfont.render(text, True, color)
    elif size == "medium":
        textSurface = mediumfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

"""Puts the message on the screen - Megan"""
def message_to_screen(message, color, y_displace=0, size = "small"):
    #puts a message on the screen
    textSurf, textRect = text_objects(message, color, size)
    textRect.center = (display_w/2), (display_h/2)+y_displace
    screen.blit(textSurf, textRect)

"""Labels the button - Megan"""
def button_word(message, color, buttonx, buttony, buttonwidth, buttonheight, y_displace=0, size='small'):
    #Puts the word on the button, called by button
    textSurf, textRect = text_objects(message, color, size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    screen.blit(textSurf, textRect)

"""Creates the button and tests for mouse location on button
-Megan"""
def button(text, x, y, width, height, inactive_color, active_color, action = None):
    #Creates a button
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #determines if mouse is over button
    #depending on which button is clicked, does different actions
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            """Hayden contributed to the sound portion to the code"""
            if action == "Quit":
                pygame.mixer.Sound('buttonpress_sfx.ogg').play()
                pygame.time.wait(500)
                pygame.quit()
                quit()
            if action == "Instructions":
                pygame.mixer.Sound('buttonpress_sfx.ogg').play()
                start = False
                game_instructions()
            if action == "Play" or action == "Play Again":
                pygame.mixer.Sound('buttonpress_sfx.ogg').play()
                Controller.Controller().game()
                #Play game Function
            if action == "Main Menu":
                pygame.mixer.Sound('buttonpress_sfx.ogg').play()
                instructions = False
                start_screen()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))
    button_word(text, BLACK, x, y, width, height)

"""Gives game instructions to user - Megan"""
def game_instructions():
    #instruction screen
    instructions = True
    while instructions == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        """LIterally writes instructions to the screen"""
        screen.fill(BLACK)
        message_to_screen("Introduction:", WHITE, -200, "medium")
        message_to_screen("One morning, four plucky young CS 110", GRAY, -150, "small")
        message_to_screen("students came together with the dream of recreating", GRAY, -120, "small")
        message_to_screen("the classic game known as Breakout.", GRAY, -90, "small")
        message_to_screen("And thus BLOCKBUSTERS was born!", GRAY, -60, "small")
        message_to_screen("Instructions:", WHITE, -10, "medium")
        message_to_screen("Use the left and right arrows to move the paddle", GRAY, 40)
        message_to_screen("Press p to pause game", GRAY, 70)
        button("Play", 75, 400, 100, 50, GREEN, LIGHTGREEN, action ="Play")
        button("Main Menu", 250, 400, 150, 50, YELLOW, LIGHTYELLOW, action ="Main Menu")
        button("Quit", 475, 400, 100, 50, RED, LIGHTRED, action ="Quit")
        pygame.display.flip()
        clock.tick(15)

"""Pauses the game - Megan"""
def pause():
    #pauses the game
    message_to_screen("Paused", BLACK, -100, "large")
    paused = True
    pygame.display.flip()
    clock.tick(15)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

"""Creates start screen UI - Megan"""
def start_screen():
#This creates a start screen
    start = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)
        title = pygame.image.load('BLOCKBUSTERS.png')
        title = pygame.transform.scale(title, (500, 206))
        screen.blit(title, (70,35))
        message_to_screen("PRESS PLAY TO BEGIN", PURPLE, 50, "medsm")

        button("Play", 75, 400, 100, 50, GREEN, LIGHTGREEN, action ="Play")
        button("Instructions", 250, 400, 150, 50, YELLOW, LIGHTYELLOW, action ="Instructions")
        button("Quit", 475, 400, 100, 50, RED, LIGHTRED, action ="Quit")

        pygame.display.flip()
        clock.tick(15)

"""Creates game over screen - Megan"""
def game_over():
    #this creates a game over screen
    failure = True
    """Adds a random taunt to the game over screen - Hayden"""
    tauntlist = ["You'll do better once you learn how to play.", "You died, and it was pretty funny.", "Aren't you used to losing by now... ?",  "Pathetic...", "You look tired. Need a break?"]
    taunt = random.choice(tauntlist)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                failure = False
                pygame.quit()
                quit()

        screen.fill(BLACK)
        message_to_screen("GAME OVER", RED, -100, "large")
        message_to_screen((taunt),GRAY,-0,"medsm")
        button("Play Again", 35, 400, 150, 50, GREEN, LIGHTGREEN, action ="Play")
        button("Main Menu", 245, 400, 150, 50, YELLOW, LIGHTYELLOW, action ="Main Menu")
        button("Quit", 450, 400, 150, 50, RED, LIGHTRED, action ="Quit")

        pygame.display.flip()
        clock.tick(15)

"""Plays the UI start screen with different paths that lead to instructions,
the actual gameplay, and Quit - Megan"""
def gamePLAY():

    gamePlay = True
    while gamePlay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamePlay = False
                pygame.quit()
                quit()
            else:
                start_screen()
                #game_over()
    pygame.quit()
    quit()
