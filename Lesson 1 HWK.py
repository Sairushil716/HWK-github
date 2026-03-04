import pygame

pygame.init()


screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("My first Pygame programme!")
gray=(58,58,58)
screen.fill(gray)


x=False
screen.fill("gray")
while not x:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()



pygame.display.flip()