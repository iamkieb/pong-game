import pygame
from random import randint

orange = (150,80,18)

class Ball(pygame.sprite.Sprite):


    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(orange)
        self.image.set_colorkey(orange)

        pygame.draw.ellipse(self.image, color, [0,0,width,height])

        self.velocity = [randint(4,8), randint(-8,8)]        
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[0]

    def bouncing(self):            
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
