import pygame, math

screen = pygame.display.set_mode((800,600))

draw_on = False
StartDraw = False
last_pos = (0, 0)
color = (0, 0, 0) 
mode = 'pen'
radius = 10 
screen.fill((255, 255, 255))

def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i)/distance*dx)
        y = int(start[1] + float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)

# Function to draw a square
def draw_square(surface, color, start, end):
    width = abs(start[0] - end[0])
    height = abs(start[1] - end[1])
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    pygame.draw.rect(surface, color, (x, y, width, height))

# Function to draw a right triangle
def draw_right_triangle(surface, color, start, end):
    width = abs(start[0] - end[0])
    height = abs(start[1] - end[1])
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    points = [(x, y), (x, y + height), (x + width, y + height)]
    pygame.draw.polygon(surface, color, points)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(surface, color, start, end):
    side_length = abs(start[0] - end[0])
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    height = (3**0.5) * side_length / 2
    points = [(x, y + height), ((x + side_length) // 2, y), (x + side_length, y + height)]
    pygame.draw.polygon(surface, color, points)

# Function to draw a rhombus
def draw_rhombus(surface, color, start, end):
    width = abs(start[0] - end[0])
    height = abs(start[1] - end[1])
    x = min(start[0], end[0])
    y = min(start[1], end[1])
    points = [(x + width // 2, y), (x, y + height // 2), (x + width // 2, y + height), (x + width, y + height // 2)]
    pygame.draw.polygon(surface, color, points)

while True:
    pressed = pygame.key.get_pressed()

    # Change color based on key press
    if pressed[pygame.K_r]:
        color = (255, 0, 0)
        radius = 10
    elif pressed[pygame.K_b]:
        color = (0, 0, 255)
        radius = 10
    elif pressed[pygame.K_g]:
        color = (0, 255, 0)
        radius = 10
    elif pressed[pygame.K_p]:
        radius = 10
        color = (255, 105, 180)
    elif pressed[pygame.K_y]:
        radius = 10
        color = (255, 255, 0)
    elif pressed[pygame.K_o]:
        radius = 10
        color = (255, 165, 0)
    elif pressed[pygame.K_d]:
        radius = 10
        color = (0, 0, 0)
    elif pressed[pygame.K_v]:
        radius = 10
        color = (255, 0, 255)
    elif pressed[pygame.K_s]:
        radius = 10
        color = (0, 191, 255)  
    elif pressed[pygame.K_SPACE] or pressed[pygame.K_w]: 
        radius = 25
        color = (255, 255, 255) 

    # Change mode based on key press
    if pressed[pygame.K_1]: mode = 'pen'
    if pressed[pygame.K_2]: mode = 'circle' 
    if pressed[pygame.K_3]: mode = 'rect'  
    if pressed[pygame.K_4]: mode = 'square'  
    if pressed[pygame.K_5]: mode = 'right_triangle'  
    if pressed[pygame.K_6]: mode = 'equilateral_triangle'  
    if pressed[pygame.K_7]: mode = 'rhombus'  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if mode == 'rect':
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                StartDraw = True
                sp = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if StartDraw:
                    pos = event.pos
                    draw_square(screen, color, sp, pos)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                StartDraw = False

        elif mode == 'circle':
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                StartDraw = True
                sp = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if StartDraw:
                    pos = event.pos
                    draw_circle(screen, color, sp, pos)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                StartDraw = False

        elif mode == 'square':
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                StartDraw = True
                sp = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if StartDraw:
                    pos = event.pos
                    draw_square(screen, color, sp, pos)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                StartDraw = False

        elif mode == 'right_triangle':
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                StartDraw = True
                sp = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if StartDraw:
                    pos = event.pos
                    draw_right_triangle(screen, color, sp, pos)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                StartDraw = False

        elif mode == 'equilateral_triangle':
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                StartDraw = True
                sp = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if StartDraw:
                    pos = event.pos
                    draw_equilateral_triangle(screen, color, sp, pos)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                StartDraw = False

        elif mode == 'rhombus
