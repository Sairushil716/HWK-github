import pygame

pygame.init()


screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("My first Pygame programme!")
gray=(58,58,58)


COLOR = (0, 0, 0)
SURFACE_COLOR = (255, 255, 255)
WIDTH = 500
HEIGHT = 500

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,
        color,
        pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

rectangle = Sprite((255,0,0), 20, 30)
rectangle.rect.x = 200
rectangle.rect.y = 300

all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(rectangle)


running=True

while running==True:
    rectangle = Sprite((255,0,0), 20, 30)
rectangle.rect.x = 200
rectangle.rect.y = 300

all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(rectangle)


pygame.quit()