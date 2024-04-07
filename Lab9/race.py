import pygame, sys, random, time
pygame.init()

FramePerSec = pygame.time.Clock()
FramePerSec.tick(60) 

white = (255, 255, 255)

speed, score, cash = 5, 0, 0
height = 600
width = 400
window = (width, height)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("lab8 game")

background = pygame.image.load("img\\Street.png")
coin = pygame.image.load("img\\Coin1.png")
player = pygame.image.load("img\\Player.png")
enemy = pygame.image.load("img\\Enemy.png") 
screen.blit(background, (0, 0))

# Class definitions

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__() 
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 5 and pressed[pygame.K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if self.rect.right < width - 5 and pressed[pygame.K_RIGHT]:        
            self.rect.move_ip(speed, 0)
        if self.rect.top > 5 and pressed[pygame.K_UP]:
            self.rect.move_ip(0, -speed)
        if self.rect.bottom < height - 5 and pressed[pygame.K_DOWN]:        
            self.rect.move_ip(0, speed)
            
    def draw(self):
        screen.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, 370), -15)
        self.weight = random.randint(1, 3)  # Assigning random weight to the coin
    
    def move(self):
        self.rect.move_ip(0, 6)
        if self.rect.top > 600:
            self.rect.center = (random.randint(15, 370), -15)

    def respawn(self):
        self.rect.center = (random.randint(30, 370), -15)        

    def draw(self):
        screen.blit(self.image, self.rect)   


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = enemy
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, width - 20), -48)       

    def move(self):
        global score, speed
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            score += 1
            self.rect.center = (random.randint(48, width - 48), -48)

    def draw(self):
        screen.blit(self.image, self.rect)


# Initializing game objects

P = Player()
E = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E)

# Create coins with different weights
coins = pygame.sprite.Group()
for _ in range(10):  # Generate 10 coins initially
    C = Coin()
    coins.add(C)

sprites = pygame.sprite.Group()
sprites.add(P)
sprites.add(E)
sprites.add(coins)

font = pygame.font.SysFont("Times New Roman", 40)

# Main game loop
pygame.display.update()
while True:
    screen.blit(background, (0, 0))
    points = font.render('Score: ' + str(score), True, (0, 0, 0))
    money = font.render('Cash:  ' + str(cash), True, (0, 0, 0))
    screen.blit(points, (10, 10))
    screen.blit(money, (10, 50))
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed_keys[pygame.K_SPACE]:
            pygame.quit()
            sys.exit()

    for sprite in sprites:
        sprite.draw()
        if isinstance(sprite, Coin):
            sprite.move()  # Move coins
        elif isinstance(sprite, Enemy):
            sprite.move()  # Move enemies

    # Check collisions
    for coin in coins:
        if pygame.sprite.collide_rect(coin, P):
            cash += coin.weight
            coin.respawn()

    if pygame.sprite.spritecollideany(P, enemies): 
        time.sleep(5)
        pygame.quit()
        sys.exit()

    # Increase speed of enemies when player earns N coins
    if cash >= 10:  # Change the value of N as needed
        speed += 1
        cash = 0  # Reset cash after increasing speed

    pygame.display.update()
    FramePerSec.tick(60)
