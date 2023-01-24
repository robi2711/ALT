<<<<<<< HEAD
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
player_one = pygame.Rect(size[0]/2 - 25, size[1] - 25, 50, 50)
player_two = pygame.Rect(size[0] - 60, size[1]/1 - 100, 50, 50)
gravity = 0.7
# Y axis velocity (Player 1)
vy = 0
# X axos velocity (Player 2)
vx = 0
=======
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random

width = 95
height = 35

drunk = {
  'wallCountdown': 1500,
  'padding': 1,
  'x': int(width / 2),
  'y': int(height / 2)
}


def getLevelRow():
  return ['\u001b[32m█'] * width


level = [getLevelRow() for _ in range(height)]

while drunk['wallCountdown'] >= 0:
  x = drunk['x']
  y = drunk['y']

  if level[y][x] == '\u001b[32m█':
    level[y][x] = '\u001b[34m█'
    drunk['wallCountdown'] -= 1

  roll = random.randint(1, 4)

  if roll == 1 and x > drunk['padding']:
    drunk['x'] -= 1

  if roll == 2 and x < width - 1 - drunk['padding']:
    drunk['x'] += 1

  if roll == 3 and y > drunk['padding']:
    drunk['y'] -= 1

  if roll == 4 and y < height - 1 - drunk['padding']:
    drunk['y'] += 1

for row in level:
  print(''.join(row))

arr = np.array([[1, 0] * 200, [0, 1] * 200] * 200)
plt.imsave("img.png", arr, cmap="Blues")
>>>>>>> 9da59c0a783a45224ac9a0e16d72a77e145494a8

# Top Boundaries Variables
top_boundary = 0
bottom_boundary = size[1] - player_one.height
on_bottom_boundry = True

<<<<<<< HEAD
# Side Boundaries Variables
left_boundary = 25
right_boundary = size[0] - 25
on_left_boundry = False
on_right_boundry = True

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
            if on_bottom_boundry:
                    vy = -15
    else:
        w_pressed = False
    # S Controller
    if keys[pygame.K_s]:
        s_pressed = True
    else:
        s_pressed = False
    # Right Controller
    if keys[pygame.K_RIGHT]:
        if not right_pressed:
            right_pressed = True
            if on_left_boundry:
                vx = 15
    else:
        right_pressed = False
    # Left Controller
    if keys[pygame.K_LEFT]:
        if not left_pressed:
            left_pressed = True
            if on_right_boundry:
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
        on_bottom_boundry = True
    else:
        on_bottom_boundry = False
    # Boundries P2
    if player_two.right >= right_boundary:
        player_two.right = right_boundary
        vx = 0
        on_right_boundry = True
    else:
        on_right_boundry = False
    if player_two.left <= left_boundary:
        player_two.left = left_boundary
        vx = 0
        on_left_boundry = True
    else:
        on_left_boundry = False
    # Final additions

    screen.blit(background_image, [0, 0])
    pygame.draw.rect(screen, (255, 0, 0), player_one)
    pygame.draw.rect(screen, (0, 0, 255), player_two)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
=======
new_image = []
for item in d:

  # change all white (also shades of whites)
  # pixels to yellow
  if item[0] in list(range(200, 256)):
    new_image.append((0, 255, 0))
  else:
    new_image.append(item)
img.putdata(new_image)

# save new image
img.save("flower_image_altered.png")
>>>>>>> 9da59c0a783a45224ac9a0e16d72a77e145494a8
