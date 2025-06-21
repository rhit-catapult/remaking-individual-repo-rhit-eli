import pygame
import sys
import random
import time

# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.color
        self.x = x
        self.y = y
        self.x_speed = random.randint(1, 5)
        self.y_speed = random.randint(1, 5)

    def color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def collide(self):
        caption = (screen.get_width() - caption1.get_width())



# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y


# TODO: Methods: __init__, draw, move



def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        # TODO: Draw the ball

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
