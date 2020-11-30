import pygame
from pygame import mixer
import players
import ball

P1 = players.Player(0, 290)
P2 = players.Player(795, 290)
Ball = ball.Ball()
Ball.rect.x = 400
Ball.rect.y = 300

pygame.init()                                   #Initializes the pygame engine
screen = pygame.display.set_mode((800, 600))    #Set the resolution of the window
pygame.display.set_caption("Pong")              #Sets the title of the window

clock = pygame.time.Clock()                     #Controls the refresh rate of the contents of the window

status = True

mixer.init()
mixer.music.load("beep.mp3")
mixer.music.set_volume(0.9)


sprite_list = pygame.sprite.Group()
sprite_list.add(P1)
sprite_list.add(P2)
sprite_list.add(Ball)

while status:                                    #Start of the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

    sprite_list.update()
    keyPress = pygame.key.get_pressed()
    if keyPress[pygame.K_w]:
        P1.moveUp(10)
    if keyPress[pygame.K_s]:
        P1.moveDown(10)
    if keyPress[pygame.K_UP]:
        P2.moveUp(10)
    if keyPress[pygame.K_DOWN]:
        P2.moveDown(10)  
    
    if Ball.rect.x >= 800:
        mixer.music.play()
        P1.score += 1
        Ball.velocity[0] = -Ball.velocity[0]
    if Ball.rect.x <0:
        mixer.music.play()
        P2.score += 1
        Ball.velocity[0] = -Ball.velocity[0]
    if Ball.rect.y < 0:
        Ball.velocity[1] = -Ball.velocity[1]
    if Ball.rect.y > 600:
        Ball.velocity[1] = -Ball.velocity[1]

    if pygame.sprite.collide_mask(Ball, P1) or pygame.sprite.collide_mask(Ball, P2):
        Ball.collide()


    screen.fill((0, 0, 0))                      #Fill the screen with black colour. Black is defined in 8-bit RGB as (0, 0, 0)
    pygame.draw.line(screen, (255, 255, 255), [400, 0], [400, 600], 1)                  #Draws a line of while colour of thickness 7 at the centre of screen
    sprite_list.draw(screen) 

    font = pygame.font.Font(None, 64)
    text = font.render(str(P1.score), 1, (255, 255, 255))
    screen.blit(text, (200, 10))
    text = font.render(str(P2.score), 1, (255, 255, 255))
    screen.blit(text, (600, 10))
    pygame.display.flip()
    clock.tick(60)
 




pygame.quit()


