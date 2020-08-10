import pygame
pygame.init()
screenbiggo = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("CoolGame")
x = 500
y = 500
vel = 50
z = 100
s = 50
run = True
herhtf = 52
g = 5
while run:
    pygame.time.delay(500)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pressingkeycont = pygame.key.get_pressed()
    if pressingkeycont[pygame.K_LEFT]:
        x-= vel
    if pressingkeycont[pygame.K_RIGHT]:
        x+= vel
    if pressingkeycont[pygame.K_DOWN]:
        y+= vel
    if pressingkeycont[pygame.K_UP]:
        y-= vel

    screenbiggo.fill((51, 223, 255))
         
    pygame.draw.circle(screenbiggo, (100, 50, 31), (x, y), 100)
    

    
    
    pygame.display.update()
    
pygame.quit()
    

    

