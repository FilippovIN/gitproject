import pygame

pygame.init()

size = width, height = 300, 300
screen = pygame.display.set_mode(size)


def draw():
    rect_color = pygame.Color('Brown')
    rect_width = 0
    rect_point = ((80, 20), (8, 250))
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

    rect_color = pygame.Color('Red')
    rect_width = 0
    rect_point = ((88, 111), (150, 40))
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
