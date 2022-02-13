# Importing libraries and initializing pygame engine
import pygame
from paddle_class import Paddle
from ball_class import Ball

pygame.init()

# ALl caps are used for constant values
# Defining colors
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
RED = (255, 0, 0)
LILA = (195, 60, 240)
YELLOW = (245, 235, 42)
PINK = (255, 204, 229)

# Loading background image
background = pygame.image.load("background.png")
# Loading music
sound = pygame.mixer.Sound("bachhoov_kev.mp3")

# Creating the screen
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Pong")


# Creating the ball
ball = Ball(RED)
ball.rect.x = 445
ball.rect.y = 245

# We need clock to control FPS
clock = pygame.time.Clock()

# Initializing scores
player_score = 0
computer_score = 0


# Creating the paddles
paddle_a = Paddle(LILA, 10, 55)
paddle_a.rect.x = 50
paddle_a.rect.y = 250

paddle_b = Paddle(YELLOW, 10, 55)
paddle_b.rect.x = 850
paddle_b.rect.y = 250

paddle_c = Paddle(YELLOW, 35, 5)
paddle_c.rect.x = 450
paddle_c.rect.y = 125

paddle_d = Paddle(YELLOW, 35, 5)
paddle_d.rect.x = 450
paddle_d.rect.y = 375

paddle_e = Paddle(YELLOW, 5, 5)
paddle_e.rect.x = 450
paddle_e.rect.y = 200

# Creating the list to hold all the sprites, and adding paddles A and B
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle_a)
all_sprites_list.add(paddle_b)
all_sprites_list.add(paddle_c)
all_sprites_list.add(paddle_d)
all_sprites_list.add(paddle_e)
all_sprites_list.add(ball)


game_on = True
# Main game loop
while game_on:
    # Main event loop
    for event in pygame.event.get():    # User did something
        if event.type == pygame.QUIT:    # Exiting the game
            game_on = False

    # Moving the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_a.move_up(10)
    if keys[pygame.K_s]:
        paddle_a.move_down(10)

    # Code for computer Ai
    if ball.rect.y > paddle_b.rect.y and (paddle_b.rect.x-ball.rect.x) < 250:
        paddle_b.rect.y += 5
    if ball.rect.y < paddle_b.rect.y and (paddle_b.rect.x-ball.rect.x) < 250:
        paddle_b.rect.y -= 5

    if ball.rect.y > paddle_e.rect.y and paddle_e.rect.y < 300:
        paddle_e.rect.y += 3
    if ball.rect.y < paddle_e.rect.y and paddle_e.rect.y > 200:
        paddle_e.rect.y -= 3

    if ball.rect.x > paddle_c.rect.x and paddle_c.rect.x < 550:
        paddle_c.rect.x += 3
    if ball.rect.x < paddle_c.rect.x and paddle_c.rect.x > 350:
        paddle_c.rect.x -= 3

    if ball.rect.x > paddle_d.rect.x and paddle_d.rect.x < 550:
        paddle_d.rect.x += 3
    if ball.rect.x < paddle_d.rect.x and paddle_d.rect.x > 350:
        paddle_d.rect.x -= 3

    # Check if the ball is bouncing of the wall
    if ball.rect.x >= 890:
        player_score += 1
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 300

    if ball.rect.x <= 10:
        computer_score += 1
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 250

    if ball.rect.y >= 490:
        ball.velocity[1] = -ball.velocity[1]

    if ball.rect.y <= 5:
        ball.velocity[1] = -ball.velocity[1]

    # Detect collisions between ball and paddles
    if pygame.sprite.collide_mask(ball, paddle_a):
        ball.bounce()
    if pygame.sprite.collide_mask(ball, paddle_b):
        ball.bounce()
    if pygame.sprite.collide_mask(ball, paddle_c):
        ball.bounce()
    if pygame.sprite.collide_mask(ball, paddle_d):
        ball.bounce()
    if pygame.sprite.collide_mask(ball, paddle_e):
        ball.bounce()

    screen.blit(background, (0, 0))
    pygame.mixer.Sound.play(sound)
    all_sprites_list.update()
    pygame.draw.line(screen, WHITE, [449, 0], [449, 500], 5)
    all_sprites_list.draw(screen)
    # Displaying score
    font = pygame.font.Font(None, 74)
    text = font.render(str(player_score), True, PINK)
    screen.blit(text, (300, 10))
    text = font.render(str(computer_score), True, PINK)
    screen.blit(text, (600, 10))

    # Updating display
    pygame.display.update()
    clock.tick(55)    # frame rates

pygame.quit()

