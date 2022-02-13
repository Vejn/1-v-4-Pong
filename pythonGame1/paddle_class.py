import pygame

# Colors
BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    # This class derives from Pygame "Sprite" Class

    def __init__(self, color, width, height):
        # Calling the parent(Sprite) class constructor
        super().__init__()

        # Creating the paddle
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Drawing the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetching the rectangle object that has dimensions of the image
        self.rect = self.image.get_rect()

    # Setting boundaries so paddles don't go over border
    def move_up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 450:
            self.rect.y = 450

    def move_left(self, pixels):
        self.rect.x -= pixels

    def move_right(self, pixels):
        self.rect.x += pixels
