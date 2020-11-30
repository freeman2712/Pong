import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.score = 0     #Variable to store score
        self.image = pygame.Surface([6, 70])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, WHITE, pygame.Rect(0, 0, 5, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos


    def moveDown(self, x):
        self.rect.y += x
        if self.rect.y > 530:
            self.rect.y = 530
    def moveUp(self, x):
        self.rect.y -= x
        if self.rect.y < 0:
            self.rect.y = 0
        
        

        
