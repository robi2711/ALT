# Pygame
import pygame
pygame.init()

# Look
size = (900, 500)
screen = pygame.display.set_mode(size)
fps = 60
clock = pygame.time.Clock()
background_image = pygame.image.load("background.png").convert()

# Variables
w_pressed = False
s_pressed = False
left_pressed = False
right_pressed = False
player_one = pygame.Rect(size[0]/2 - 30, size[1] - 25, 50, 50)
player_two = pygame.Rect(size[0] - 60, size[1]/1 - 100, 50, 50)
gravity = 0.7
p1_right_pos = player_one.right
# Y axis velocity (Player 1)
vy = 0
# X axos velocity (Player 2)
vx = 0

# Top Boundaries Variables
top_boundary = 0
bottom_boundary = size[1] - player_one.height
on_bottom_boundary = True

# Side Boundaries Variables
left_boundary = 25
right_boundary = size[0] - 25
on_left_boundary = False
on_right_boundary = True

# Main
running = True
while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    # W controller
    if keys[pygame.K_w]:
        if not w_pressed:
            w_pressed = True
            if on_bottom_boundary:
                vy = -15
                p1_rightpos = 2000
    else:
        w_pressed = False
        p1_rightpos = player_one.right
    # S Controller
    if keys[pygame.K_s]:
        s_pressed = True
    else:
        s_pressed = False
    # Right Controller
    if keys[pygame.K_RIGHT]:
        if not right_pressed:
            right_pressed = True
            if on_left_boundary:
                vx = 15
    else:
        right_pressed = False
    # Left Controller
    if keys[pygame.K_LEFT]:
        if not left_pressed:
            left_pressed = True
            if on_right_boundary:
                vx = -15
    else:
        left_pressed = False
    # Jumping/Falling
    if s_pressed:
        vy += gravity * 4
    else:
        vy += gravity
    player_one.y += vy
    # Left/Right
    player_two.x += vx
    
    # Boundries P1
    if player_one.top <= top_boundary:
        player_one.top = top_boundary
        vy = 0
    if player_one.bottom >= bottom_boundary:
        player_one.bottom = bottom_boundary
        vy = 0
        on_bottom_boundary = True
    else:
        on_bottom_boundary = False
    # Boundries P2
    if player_two.right >= right_boundary:
        player_two.right = right_boundary
        vx = 0
        on_right_boundary = True
    else:
        on_right_boundary = False
    if player_two.left <= left_boundary:
        player_two.left = left_boundary
        vx = 0
        on_left_boundary = True
    else:
        on_left_boundary = False
    # Kill Boxes
    if player_two.right == p1_rightpos:
        print("L")
    print(p1_rightpos)
    print(player_two.right)
    # Final additions

    screen.blit(background_image, [0, 0])
    pygame.draw.rect(screen, (255, 0, 0), player_one)
    pygame.draw.rect(screen, (0, 0, 255), player_two)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
