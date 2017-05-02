import pygame, sys


class Visuals:
    pygame.font.init()
    pygame.display.init()

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
    midnight = (25, 25, 112)
    purple = (148, 0, 211)
    gray = (139, 139, 131)

    #font options
    smallfont = pygame.font.SysFont('serif', 25, bold=True)
    mediumfont = pygame.font.SysFont('serif', 50, bold=True)
    largefont = pygame.font.SysFont('serif', 80, bold=True)

    def __init__(self, display_w, display_h):
        #self.screen = screen
        self.display_w = display_w
        self.display_h = display_h

    def jukebox(self):
        #lets us add music and sound effects
        pygame.mixer.music.load('OST.mp3')
        pygame.mixer.music.play(-1)

    def text_objects(self, text, color, size):
        #Called by message_to_screen, needed to create an on screen message

        if size == "small":
            textSurface = Visuals.smallfont.render(text, True, color)
        elif size == "medium":
            textSurface = Visuals.mediumfont.render(text, True, color)
        elif size == "large":
            textSurface = Visuals.largefont.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def message_to_screen(self, message, color, y_displace, size="small"):
        #puts a message on the screen
        textSurf, textRect = Visuals.text_objects(message, color, y_displace, size)
        textRect.center = (display_w/2), (display_h/2)+y_displace
        screen.blit(textSurf, textRect)

    def button_word(self, color, buttonx, buttony, buttonwidth, buttonheight, size='small'):
        #Puts the word on the button, called by button
        textSurf, textRect = Visuals.text_objects(message, color, size)
        textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
        screen.blit(textSurf, textRect)

    def button(self, text, x, y, width, height, inactive_color, active_color, action = None):
        #Creates a button
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #determines if mouse is over button
        #depending on which button is clicked, does different actions
        if x + width > cursor[0] > x and y + height > cursor[1] > y:
            pygame.draw.rect(screen, active_color, (x, y, width, height))
            if click[0] == 1 and action != None:
                if action == "Quit":
                    pygame.quit()
                    quit()
                if action == "Instructions":
                    game_instructions()
                if action == "Play" or action == "Play Again":
                    pass
                    #Play game Function
                if action == "Main Menu":
                    start_screen()
        else:
            pygame.draw.rect(screen, inactive_color, (x, y, width, height))
        Visuals.button_word(text, Visuals.black, x, y, width, height)

    def game_instructions(self):
        #instruction screen
            screen.fill(Visuals.midnight)
            Visuals.message_to_screen("BLOCKBUSTERS", Visuals.blue, -250, "medium")
            Visuals.message_to_screen("Introduction: One morning, four plucky young CS 110 students", Visuals.gray, -200, "small")
            Visuals.message_to_screen("came together with the dream of recreating the classic game", Visuals.gray, -170, "small")
            Visuals.message_to_screen("known as Breakout. And thus BLOCKBUSTERS was born!", Visuals.gray, -140, "small")
            Visuals.message_to_screen("Instructions:", Visuals.white, -50, "medium")
            Visuals.message_to_screen("Use the left and right arrows to move the paddle", Visuals.gray, 0)
            Visuals.message_to_screen("Press p to pause game", Visuals.gray, 40)
            Visuals.button("Play", 150, 500, 100, 50, Visuals.green, Visuals.lightgreen, action = "Play")
            Visuals.button("Main Menu", 325, 500, 150, 50, Visuals.yellow, Visuals.lightyellow, action = "Main Menu")
            Visuals.button("Quit", 550, 500, 100, 50, Visuals.red, Visuals.lightred, action = "Quit")
            #pygame.display.flip()
            #clock.tick(15)

    def pause(self):
        #pauses the game
        Visuals.message_to_screen("Paused", Visuals.black, -100, "large")
        paused = True
        #pygame.display.flip()
        #clock.tick(15)
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False

    def start_screen(self, screen):
        #This creates a start screen
        screen.fill(Visuals.midnight)
        Visuals.message_to_screen("BLOCKBUSTERS", Visuals.blue, -100, "large")
        Visuals.message_to_screen("PRESS PLAY TO BEGIN", Visuals.purple, 50, "medium")

        Visuals.button("Play", 150, 500, 100, 50, Visuals.green, Visuals.lightgreen, action = "Play")
        Visuals.button("Instructions", 325, 500, 150, 50, Visuals.yellow, Visuals.lightyellow, action = "Instructions")
        Visuals.button("Quit", 550, 500, 100, 50, Visuals.red, Visuals.lightred, action = "Quit")

        #pygame.display.flip()
        #clock.tick(15)

    def game_over(self):
        #this creates a game over screen
        screen.fill(Visuals.black)
        message_to_screen("GAME OVER", Visuals.red, -100, "large")
        button("Play Again", 110, 500, 150, 50, Visuals.green, Visuals.lightgreen, action = "Play")
        button("Main Menu", 325, 500, 150, 50, Visuals.yellow, Visuals.lightyellow, action = "Main Menu")
        button("Quit", 550, 500, 150, 50, Visuals.red, Visuals.lightred, action = "Quit")

        #pygame.display.flip()
        #clock.tick(15)
class GUI:
    def __init__(self):
        self.display_w = 640
        self.display_h = 480
        self.v = Visuals(self.display_w, self.display_h)

    def gui(self):
        pygame.init()
        screen = pygame.display.set_mode((self.display_w, self.display_h))
        clock = pygame.time.Clock()
        pygame.display.set_caption('Blockbusters')

        self.v.start_screen(screen)


        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True


            pygame.display.flip()
            clock.tick(15)

        pygame.quit()
        quit()

if __name__ == '__main__':
    run = GUI()
    run.gui()
