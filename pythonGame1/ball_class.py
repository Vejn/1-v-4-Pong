import pygame
from random import randint

BLACK = (0, 0, 0)


# This class represents a ball
class Ball(pygame.sprite.Sprite):

    def __init__(self, color):
        # Call the parent class constructor
        super().__init__()

        self.image = pygame.Surface([8, 8])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball(rectangle)
        pygame.draw.rect(self.image, color, [0, 0, 8, 8])

        self.velocity = [randint(5, 10), randint(-8, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-10, 10)
