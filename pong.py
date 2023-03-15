import pygame
import sys
from paddle import Paddle
from ball import Ball

pygame.init()

#game variables
black = (0,0,0)
white = (255,255,255)
brand = (251,80,18)


size = (600,600)
game_display = pygame.display.set_mode(size)
pygame.display.set_caption('Pong')


#paddles
paddle1 = Paddle(black, 10, 100)
paddle1.rect.x = 50
paddle1.rect.y = 300

paddle2 = Paddle(black, 10, 100)
paddle2.rect.x = 550
paddle2.rect.y = 300

#ball 
ball = Ball(black,10,10)
ball.rect.x = 300
ball.rect.y = 300

#sprites
sprites_list = pygame.sprite.Group()

sprites_list.add(paddle1)
sprites_list.add(paddle2)
sprites_list.add(ball)

#score-players
score1 = 0
score2 = 0

#sound
scoring_sound1 = pygame.mixer.Sound('Hit.wav')
scoring_sound2 = pygame.mixer.Sound('Dist.wav')
poping_sound = pygame.mixer.Sound('Pop.wav')

#game conditions
game_on = True
clock = pygame.time.Clock()

while game_on: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_on = False

## add sprites
    sprites_list.update()

## key controls - baddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.paddles_move_up(7)
    if keys[pygame.K_s]:
        paddle1.paddles_move_down(7)
    if keys[pygame.K_UP]:
        paddle2.paddles_move_up(7)
    if keys[pygame.K_DOWN]:
        paddle2.paddles_move_down(7)

# sprite behaviour - ball
    if ball.rect.x >= 600:
        score1 += 1
        scoring_sound1.play()
        ball.velocity[0] = ball.velocity[0]
        ball.rect.x = 300
        ball.rect.y = 300

    if ball.rect.x <= 2:
        score2 += 1
        scoring_sound2.play()
        ball.velocity[0] = ball.velocity[0]
        ball.rect.x = 300
        ball.rect.y = 300

    if ball.rect.y > 555: 
        ball.velocity[1] = ball.velocity[1]

    if ball.rect.y < 2:
        ball.velocity[1] = ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        poping_sound.play()
        ball.bouncing()

## display 
    game_display.fill(white)

    pygame.draw.line(game_display, brand, [300,0], [300,600], 10)
    sprites_list.draw(game_display)

## scoreboard
    font = pygame.font.Font(None, 100)
    text = font.render(str(score1), 1, black) # type: ignore
    game_display.blit(text,(125,10))

    font = pygame.font.Font(None, 100)
    text = font.render(str(score2), 1, black) # type: ignore
    game_display.blit(text,(425,10))

## display fix
    pygame.display.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()