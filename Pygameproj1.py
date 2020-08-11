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
    pygame.draw.line(screenbiggo, (100, 0, 255), (0, 10), (300, 10), 10)
    all_sprites = pygame.sprite.Group()
    all_sprites.update()
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
    

    

