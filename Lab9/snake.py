import pygame, sys, random, time

pygame.init()

FPS = pygame.time.Clock() 
fps = 10
FPS.tick(fps)

White = (255, 255, 255)
LightSteelBlue = (176, 196, 222)
Red = (255, 0, 0)
Green = (0, 255, 0) 

height = 500
width = 500
window = (width, height)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Lab8 Snake") 
step = 20

direction = 'RIGHT'

End = False 
append = False 

background=pygame.transform.scale(pygame.image.load('img\\background.png'),(600,600)) 
coin=pygame.transform.scale(pygame.image.load("img\\Coin1.png"),(20,20)) 
font=pygame.font.SysFont('Times New Roman', 24)
score=0  
body=[] 
head_x = head_y=240
step=20 
move_x,move_y=20,0 
direction =  'RIGHT' 

# Function to generate random food coordinates
def rand():
    return (random.randint(2, 22) * 20)

coin_x = rand()
coin_y = rand()

# Timer variables for food disappearance
food_timer = 100  # Food disappearance timer
start_time = pygame.time.get_ticks()

while True:
    FPS.tick(fps)
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed[pygame.K_SPACE]:
            pygame.quit()
            sys.exit() 

        if pressed[pygame.K_DOWN]: 
            if direction != 'UP': 
                direction = 'DOWN' 
                move_x = 0 
                move_y = step 

        if pressed[pygame.K_UP]: 
            if direction != 'DOWN':
                direction = 'UP'
                move_x = 0
                move_y = -step

        if pressed[pygame.K_LEFT]:
            if direction != 'RIGHT':
                direction = 'LEFT'
                move_x = -step
                move_y = 0

        if pressed[pygame.K_RIGHT]: 
            if direction != 'LEFT':
                direction = 'RIGHT'
                move_x = step
                move_y = 0    

    if not End:    
        body.append([head_x, head_y]) 
        body.pop(0) 
        if append:
            body.append([head_x, head_y]) 
            score += 1 
            append = False
        head_x += move_x 
        head_y += move_y

        # Check if the snake hits the wall
        if head_x < 0 or head_x > 480 or head_y < 0 or head_y > 480: 
            End = True 

        # Adjust FPS based on score
        fps = 10 + score

        # Check if the snake eats the food
        if head_x == coin_x and head_y == coin_y:
            coin_x = rand()
            coin_y = rand()
            append = True
            start_time = pygame.time.get_ticks()  # Reset food timer

        # Check food disappearance based on timer
        elapsed_time = pygame.time.get_ticks() - start_time
        if elapsed_time > food_timer:
            coin_x = rand()
            coin_y = rand()
            start_time = pygame.time.get_ticks()  # Reset food timer

        screen.blit(background, (0, 0)) 
        screen.blit(coin, (coin_x, coin_y))
        pygame.draw.rect(screen, (0, 100, 0), (head_x, head_y, 20, 20))

        for block in body:
            if head_x == block[0] and head_y == block[1]: 
                End = True 
                break 
            pygame.draw.rect(screen, (0, 200, 0), (block[0], block[1], 20, 20)) 
            screen.blit(font.render("Score: {}".format(score), True, (255, 0, 0)), (10, 10)) 
    else: 
        screen.fill((255, 255, 255)) 
        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (175, 200)) 
    pygame.display.update()
