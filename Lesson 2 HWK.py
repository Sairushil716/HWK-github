import pygame

window=pygame.display.set_mode((400,400))

window.fill((255,255,255))

GREEN=(0,255,0)
BLACK=(0,0,0)
x=0
y=0
pygame.draw.rect(window,GREEN,(100,100,100,100))

pygame.draw.rect(window,BLACK,(100,100,50,10))

pygame.display.update()

done=False

while not done:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                done=True
    
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-=3
        if pressed[pygame.K_RIGHT]: x+=3
        if pressed[pygame.K_UP]: y-=3
        if pressed[pygame.K_DOWN]: y+=3

        

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()