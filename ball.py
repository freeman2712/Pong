import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([8, 8])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, (255, 255, 255), [0, 0, 8, 8])
        self.velocity = [random.randint(4, 8), random.randint(-8, 8)]
        


        self.rect = self.image.get_rect()


    def update(self):
        self.rect.x +=self.velocity[0]
        self.rect.y +=self.velocity[1]

    def collide(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8, 8)
        

        
