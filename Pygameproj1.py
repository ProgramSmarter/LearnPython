import pygame
pygame.init()
screenbiggo = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("CoolGame")
x = 50
y = 100
width = 40
height = 60
vel = 10
run = True
while run:
    pygame.time.delay(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.circle(screenbiggo, (100, 50, 31), (x, y, width, height))
    pygame.display.update()
pygame.quit()
