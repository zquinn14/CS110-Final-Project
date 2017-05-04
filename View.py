import pygame, sys

pygame.init()

display_w = 640
display_h = 480

screen = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption('Blockbusters')

clock = pygame.time.Clock()

#these need to be moved I think
pygame.mixer.music.load('OST.mp3')
pygame.mixer.music.play(-1)

#color options
white = (255, 255, 255)
black = (0, 0, 0)
lightred = (250, 40, 10)
red = (255, 0 ,0)
lightgreen = (50, 205, 50)
green = (0, 100, 0)
yellow = (255, 165, 0)
lightyellow = (255, 255, 0)
blue = (60, 179, 113)
purple = (148, 0, 211)
gray = (139, 139, 131)

#font options
smallfont = pygame.font.SysFont('serif', 25, bold=True)
mediumfont = pygame.font.SysFont('serif', 50, bold=True)
largefont = pygame.font.SysFont('serif', 80, bold=True)


def text_objects(text, color, size):
    #called by message_to_screen, needed to write the text
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = mediumfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(message, color, y_displace=0, size = "small"):
    #puts a message on the screen
    textSurf, textRect = text_objects(message, color, size)
    textRect.center = (display_w/2), (display_h/2)+y_displace
    screen.blit(textSurf, textRect)

def button_word(message, color, buttonx, buttony, buttonwidth, buttonheight, y_displace=0, size='small'):
    #Puts the word on the button, called by button
    textSurf, textRect = text_objects(message, color, size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    screen.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    #Creates a button
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #determines if mouse is over button
    #depending on which button is clicked, does different actions
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
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
                #Play game Function
            if action == "Main Menu":
                pygame.mixer.Sound('buttonpress_sfx.ogg').play()
                instructions = False
                start_screen()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))
    button_word(text, black, x, y, width, height)

def game_instructions():
    #instruction screen
    instructions = True
    while instructions == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)
        message_to_screen("BLOCKBUSTERS", blue, -250, "medium")
        message_to_screen("Introduction: One morning, four plucky young CS 110 students", gray, -200, "small")
        message_to_screen("came together with the dream of recreating the classic game", gray, -170, "small")
        message_to_screen("known as Breakout. And thus BLOCKBUSTERS was born!", gray, -140, "small")
        message_to_screen("Instructions:", white, -50, "medium")
        message_to_screen("Use the left and right arrows to move the paddle", gray, 0)
        message_to_screen("Press p to pause game", gray, 40)
        button("Play", 150, 500, 100, 50, green, lightgreen, action = "Play")
        button("Main Menu", 325, 500, 150, 50, yellow, lightyellow, action = "Main Menu")
        button("Quit", 550, 500, 100, 50, red, lightred, action = "Quit")
        pygame.display.flip()
        clock.tick(15)

def pause():
    #pauses the game
    message_to_screen("Paused", black, -100, "large")
    paused = True
    pygame.display.flip()
    clock.tick(15)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

def start_screen():
#This creates a start screen
    start = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)
        message_to_screen("BLOCKBUSTERS", blue, -100, "large")
        message_to_screen("PRESS PLAY TO BEGIN", purple, 50, "medium")

        button("Play", 150, 500, 100, 50, green, lightgreen, action = "Play")
        button("Instructions", 325, 500, 150, 50, yellow, lightyellow, action = "Instructions")
        button("Quit", 550, 500, 100, 50, red, lightred, action = "Quit")

        pygame.display.flip()
        clock.tick(15)

def game_over():
    #this creates a game over screen
    failure = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                failure = False
                pygame.quit()
                quit()

        screen.fill(black)
        message_to_screen("GAME OVER", red, -100, "large")
        button("Play Again", 110, 500, 150, 50, green, lightgreen, action = "Play")
        button("Main Menu", 325, 500, 150, 50, yellow, lightyellow, action = "Main Menu")
        button("Quit", 550, 500, 150, 50, red, lightred, action = "Quit")

        pygame.display.flip()
        clock.tick(15)

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

#gamePLAY()
