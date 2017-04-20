import pygame
import sys

pygame.init

class Screen:
    def __init__(self):
        pygame.init()
        screen_size = 1080,720
        self.screen = pygame.display.set_mode(screen_size)
        self.font = pygame.font.Font(None, 30)

class Paddle_and_Ball:
    def __init__(self):
        balldiamter = 16
        ballheight = 12
        ballradius = 6
        paddley = 720 - 12 - 10
        self.state = 0 #in Paddle
        self.paddle = pygame.Rect(300, 720-22, 60, 12) #second value is screensize - paddle height(last value) - 10
        self.ball = pygame.Rect(300, 698 - 16, 16, 16) #second value is the second value from paddle - ball diameter (16)
        self.ballVelocity = [5,-5]


    def key_press(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.paddle.left -= 5
            if self.paddle.left < 0:
                self.paddle.left = 0

        if keys[pygame.K_RIGHT]:
            self.paddle.left += 5
            if self.paddle.left > 1020: #(screensize - paddlewidth):
                self.paddle.left = 1020

        if keys[pygame.K_SPACE] and self.state == 0:
            self.ballVelocity = [5,-5]
            self.state = 1 #playing
        elif keys[pygame.K_RETURN] and (self.state == 3 or self.state == 2): #3 is game over and 2 is won
                """not sure how to make this restart using the game class"""

    def ball_movement(self):
        self.ball.left += self.ballVelocity[0]
        self.ball.top += self.ballVelocity[1]

        if self.ball.left <= 0:
            self.ball.left = 0
            self.ballVelocity[0] = -self.ballVelocity[0]
        elif self.ball.left >= 1064:
            self.ball.left = (1064)
            self.ballVelocity[0] = -self.ballVelocity[0]

        if self.ball.y < 0:
            self.ball.top = 0
            self.ballVelocity[1] = -self.ballVelocity[1]

    def CreateBlocks(self):
        self.blocks = []
        y = 50
        for i in range(y, 200, 10):
            x = 50
            for j in range(x, 800, 25):
                block = pygame.Rect(x,y,25,10)
                self.blocks.append(block)
                x += 27
            y += 12


    def collisions(self):
        self.CreateBlocks()
        for block in self.blocks: #is that how i call this variable from another class?
            if self.ball.colliderect(block):
                Game.self.score += 3
                self.ballVelocity[1] = -self.ballVelocity[1]
                Bricks.self.remove(block)
                break

        if len(self.blocks) == 0:
            self.state = 2 #won state

        if self.ball.colliderect(self.paddle):
            self.ball.top = 682
            self.ballVelocity[1] = -self.ballVelocity[1]
        elif self.ball.top > self.paddle.top:
            Game.self.lives -= 1
            if Game.self.lives > 0:
                self.state = 0
            else:
                self.state = 3
class Game:
    def __init__(self):
        self.lives = 4
        self.score = 0
        c = Paddle_and_Ball()
        c.CreateBlocks()

    def run(self):
        s = Screen()
        black = 255,255,255
        blue = 0,0,255
        green = 0,255,0
        while 1:
            play = Paddle_and_Ball()
            # if pygame.key.get_pressed()[pygame.K_q]:
            #     pygame.quit()
            s.screen.fill(black)
            play.key_press()
            if play.state == 1:
                play.ball_movement()
                play.collisions()
            if play.state == 0:
                play.ball.left = play.paddle.left + play.paddle.width / 2
                play.ball.top = play.paddle.top - play.ball.height
            elif play.state == 3:
                self.show_message('GAME OVER')
            elif play.state == 2:
                self.show_message('YOU WON')


            play.CreateBlocks()

            pygame.draw.rect(s.screen, blue, play.paddle)

            pygame.draw.circle(s.screen, green, (play.ball.left + 8, play.ball.top + 8), 8)

            pygame.display.flip()

class Bricks:
    	def __init__(self):
    		self.blocks = []


if __name__ == '__main__':
    Screen().__init__()
    Bricks().__init__()
    Paddle_and_Ball().key_press()
    Paddle_and_Ball().collisions()
    Paddle_and_Ball().ball_movement()
    Game().run()
