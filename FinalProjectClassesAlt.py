import pygame

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(1080,720)
        self.font = pygame.font.Font('Arial', 30)

class Paddle_and_Ball:
    def __init__(self):
        balldiamter = 16
        ballheight = 12
        ballradius = 6
        paddley = 720 - 12 - 10
        self.state = 0 #in Paddle
        self.paddle = pygame.Rect(300, 720-22, 60, 12) #second value is screensize - paddle height(last value) - 10
        self.ball = pygame.Rect(300, 698 - 16, 16, 16) #second value is the second value from paddle - ball diameter (16)
        self.ballVelocity = [1,-1]


        def key_press(self):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.paddle.left -= 5
                if self.paddle.left <= 0:
                    self.paddle.left = 0

            if keys[pygame.K_RIGHT]:
                self.paddle.left += 5
                if self.paddle.left >= 1080 - 60: #(screensize - paddlewidth):
                    self.paddle.left = 1080-60

            if keys[pygame.K_SPACE] and self.state == 0:
                self.ballVelocity = [1,-1]
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

        def collisions(self):
            for block in Bricks.self.blocks: #is that how i call this variable from another class?
                if self.ball.colliderect(block):
                    Game.self.score += 3
                    self.ballVelocity[1] = -self.ballVelocity[1]
                    Bricks.self.remove(block)
                    break

            if len(Bricks.self.blocks) == 0:
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
        Bricks.CreateBlocks
    def run(self):
        while 1:
            play = Paddle_and_Ball.self
            for event in pygame.event.get():
                if event.type == pygame.Quit:
                    sys.exit
            Screen.self.screen.fill('BLACK')
            play.key_press()
            if play.state == 1:
                play.ball_movement()
                play.collisions()
            if play.state == 0:
                play.ball.left = play.paddle.left + self.paddle.width / 2
                play.ball.top = self.paddle.top - self.ball.height
            elif play.state == 3:
                self.show_message('GAME OVER')
            elif play.state == 2:
                self.show_message('YOU WON')

            self.draw_bricks

            pygame.draw.rect(Screen.self.screen, BLUE, play.paddle)

            pygame.draw.circle(Screen.self.screen, GREEN, (play.ball.left + 8, play.ball.top + 8), 8)

            pygame.displat.flip()

class Bricks:
    	def __init__(self):
    		self.blocks = blocks

    	def CreateBlocks(self):
    		blocks = []
    		y = 50
    		for i in range(y, 200, 10):
    			X = 50
    			for j in range(x, 800, 25):
    				block = pygame.rectangle(x,y,25,10)
    				self.blocks.append(blocks)
    				x += 27
    			y += 12

if __name__ == '__main__':
    Screen().run()
    Bricks().run()
    Paddle_and_Ball().run
    Game().run()
