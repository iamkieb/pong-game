import pygame

orange = (251,80,18)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(orange)
        self.image.set_colorkey(orange)

        pygame.draw.rect(self.image, color, [0,0,width,height])
        
        self.rect = self.image.get_rect()

    def paddles_move_up(self, n_pixels):
        self.rect.y -= n_pixels
        if self.rect.y < 0:
            self.rect.y = 0
    
    def paddles_move_down(self, n_pixels):
        self.rect.y += n_pixels
        if self.rect.y > 600:
            self.rect.y = 600

