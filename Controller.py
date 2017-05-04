import pygame
import sys
import View
from Model import Paddle, Wall, Brick, Ball

""""COLORS"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREENISH = (0, 50, 50)
BLUEISH = (0, 255, 204)
GREY = (100, 100, 150)

class Controller(pygame.sprite.Sprite):

    """Class Variables:"""

    #Screen Dimensions
    displayDimensions = (640,480)

    #Brick Number and height from top
    topBrick = 80
    bricksNum = 12

    def __init__(self):
        super().__init__()

        """PYGAME INITIALIZATION"""
        pygame.init()

        """Setup of window or screen"""
        self.gameDisplay = pygame.display.set_mode(self.displayDimensions)
        pygame.display.set_caption('BLOCKBUSTER!')

        """SPRITE GROUPS"""
        self.bricks = pygame.sprite.Group()
        self.ballGroup = pygame.sprite.Group()
        self.allSprites = pygame.sprite.Group()

        """PADDLE"""
        self.p = Paddle()
        self.allSprites.add(self.p)

        """BALL"""
        self.b = Ball()
        self.allSprites.add(self.b)
        self.ballGroup.add(self.b)

        """WALL CREATION"""
        self.wall_list = pygame.sprite.Group()

        self.wall = Wall(-100, 430, 1, 20)
        self.wall_list.add(self.wall)
        self.allSprites.add(self.wall)

        self.wall = Wall(740, 430, 1, 20)
        self.wall_list.add(self.wall)
        self.allSprites.add(self.wall)

        self.p.walls = self.wall_list

        """BRICK CREATION - calls class variables"""
        Brick.build_bricks(self.bricks, self.bricksNum, self.topBrick, self.allSprites)

        """Initialize state value"""
        self.state = 0

        """SCORE KEEPING"""
        self.score = 0

    """MEthod that when called will bring user to start_screen - Starts UI Experience"""
    def play(self):
        View.start_screen()

    """Method that will play the game"""
    def game(self):
        clock = pygame.time.Clock()
        tinyfont = pygame.font.SysFont('serif', 12, bold=True)
        gameExit = False

        """GAME LOOP"""
        while True:

            clock.tick(60)
            self.gameDisplay.fill(GREENISH)

            """GAME SCORE"""
            scoreD = tinyfont.render('Score: {}'.format(self.score), 1, WHITE)
            scoreDpos = scoreD.get_rect(centerx = 600)
            scoreDpos.bottom = 466
            self.gameDisplay.blit(scoreD, scoreDpos)

            """Event Loop"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                """Pauses Game - state changes to 2"""
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p and self.state == 1:
                        View.pause()

            """COLLISION HANDLING"""
            if pygame.sprite.spritecollide(self.p, self.ballGroup, False):
                control = (self.p.rect.x + self.p.paddleWidth / 2) - (self.b.rect.x + self.b.ballRadius / 2)
                self.b.rect.y = 432
                self.b.rebound(control)

                """Helps make ball bounce smoothly off paddle"""
                if not gameExit:
                    gameExit = self.b.update(self.state)

            """Displays GAME OVER"""
            if len(self.bricks) != 0 and self.b.rect.y > 440:
                gameExit = True
                View.game_over()

            """Allows Ball to rebound off bricks - and counts the score"""
            hitBlocks = pygame.sprite.spritecollide(self.b, self.bricks, True)
            if len(hitBlocks) > 0:
                self.b.rebound(0)
                self.score += 100

            """HANDLES a WIN"""
            if len(self.bricks) == 0:
                start_again = Controller()
                start_again.game()

            """PADDLE CONTROL"""
            #try/except handles an error that may occur when restarting the game after a win
            try:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        key_press = 0
                        self.p.movePaddle(key_press)
            except UnboundLocalError:
                start_again = Controller()
                start_again.game()

            keys = pygame.key.get_pressed()

            """KEYS PRESSED - changes state & moves paddle"""
            if keys[pygame.K_LEFT] and self.state == 1:
                key_press = 1
                self.p.movePaddle(key_press)
            elif keys[pygame.K_RIGHT] and self.state == 1:
                key_press = 2
                self.p.movePaddle(key_press)
            elif keys[pygame.K_SPACE] and self.state == 0:
                self.state = 1

            """WRAP PADDLE - dope feature that puts the paddle from one side to another through the walls:
            hence the wrap"""
            paddle_collision_checks = pygame.sprite.spritecollide(self.p, self.wall_list, False)
            for i in paddle_collision_checks:
                if self.p.paddle_x_change > 0:#MOVING TO THE RIGHT
                    self.p.rect.x = 0
                else:
                    self.p.rect.x = self.displayDimensions[0] - self.p.paddleWidth

            self.allSprites.draw(self.gameDisplay)

            """If statement --> when game is active, paddle can move"""
            if not gameExit:
                self.p.rect.x += (self.p.paddle_x_change)

            self.b.update(self.state)

            pygame.display.update()

        pygame.quit
        quit()

if __name__ == '__main__':
    run = Controller()
    run.play()
