# Imports
import random
import pygame
import time
import matplotlib.pyplot as plt

# Functions
def fw(name, write):
    file = open(name, "w")
    file.write(write)
    file.close


def fa(name, write):
    file = open(name, "a")
    file.write(write)
    file.close


def fr(name):
    file = open(name, "r")
    return file.read()
    file.close

def mean(name):
    ##Gets mean
    total = 0
    counter = 0
    while counter != len(name):
        total += int(name[counter])
        counter += 1
    mean = total/counter
    counter = 0
    return mean
# Variables
main_run = False
w_pressed = False
s_pressed = False
left_pressed = False
right_pressed = False
singleplayer = False
multiplayer = False
simulation = False
start_menu = True

clear = input("Would you like to clear the data? ((y/n) NOTE! only do this if you are sure as it is not reversable!): ")
if clear == "y":
    fw(scores, "")
elif clear == "n":
    print("Ok")
else:
    print("Invalid input, taking youre answer as a no :)")
while True:
    try:
        dvx = int(input("Pick a number that changes the speed of player two (20 is reccomended): "))
        break
    except:
        print("That's not a valid option!")
# Look
pygame.init()
pygame.display.set_caption("Q-Bits")
size = (900, 500)
screen = pygame.display.set_mode(size)
fps = 60
clock = pygame.time.Clock()
background_image = pygame.image.load("background.png").convert()
player_one = pygame.Rect(size[0]/2 - 30, size[1] - 25, 50, 50)
player_two = pygame.Rect(size[0] - 60, size[1]/1 - 100, 50, 50)

# Movement
#-Y axis velocity (Player 1)
vy = 0
#-X axos velocity (Player 2)
vx = 2
gravity = 0.7
p1_right_pos = player_one.right

# Boundries
# Top Boundaries Variables
top_boundary = 0
bottom_boundary = size[1] - player_one.height
on_bottom_boundary = True
# Side Boundaries Variables
left_boundary = 25
right_boundary = size[0] - 25
on_left_boundary = False
on_right_boundary = True
clock = pygame.time.Clock()


# Endgame screen Variables
font = pygame.font.Font(None, 60)
text = font.render("Game Over", True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (size[0] // 2, size[1] // 2 - 50)
restart_font = pygame.font.Font(None, 36)
restart_text = restart_font.render("Restart", True, (255, 255, 255))
restart_button = restart_text.get_rect()
restart_button.center = (size[0] // 2, size[1] // 2 + 50)
exit_font = pygame.font.Font(None, 36)
exit_text = exit_font.render("Back to start menu", True, (255, 255, 255))
exit_button = exit_text.get_rect()
exit_button.center = (size[0] // 2, size[1] // 2 + 80)

# Start Menu variables
start_font = pygame.font.Font(None, 36)
start_text = font.render("Welcome to Q-Bits", True, (255, 255, 255))
start_text_rect = start_text.get_rect()
start_text_rect.center = (size[0] // 2, size[1] // 2 - 120)
singleplayer_button = pygame.Rect(250, 200, 300, 50)
multiplayer_button = pygame.Rect(250, 275, 300, 50)
stat_button = pygame.Rect(800, 450, 300, 50)
simulation_button = pygame.Rect(250, 350, 300, 50)
quit_button = pygame.Rect(0, 450, 300, 50)
quit_text = start_font.render("Quit", True, (255, 255, 255))
singleplayer_text = start_font.render("Singleplayer", True, (255, 255, 255))
stat_text = start_font.render("Stats", True, (255, 255, 255))
multiplayer_text = start_font.render("Multiplayer", True, (255, 255, 255))
simulation_text = start_font.render("Simulation", True, (255, 255, 255))

# Score System
sfile = "scores.csv"
#fw(sfile, "")
score = 0
start_time = time.time()

# Main Code
while start_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if singleplayer_button.collidepoint(event.pos):
                main_run = True
                singleplayer = True
                multiplayer = False
                simulation = False
                start_time = time.time()
            elif multiplayer_button.collidepoint(event.pos):
                main_run = True
                multiplayer = True
                singleplayer = False
                simulation = False
                start_time = time.time()
            elif simulation_button.collidepoint(event.pos):
                main_run = True
                simulation = True
                singleplayer = False
                multiplayer = False
                start_time = time.time()
            elif quit_button.collidepoint(event.pos):
                start_menu = False
            elif stat_button.collidepoint(event.pos):
                s_values = []
                m_values = []
                u_values = []
                dataIn = fr(sfile)
                dataIn = dataIn.split(", ")
                del dataIn[-1]
                for i in dataIn:
                    if i[0] == 's':
                        s_values.append(int(i[1:]))
                    elif i[0] == 'm':
                        m_values.append(int(i[1:]))
                    elif i[0] == 'u':
                        u_values.append(int(i[1:]))
                s_values.sort()
                m_values.sort()
                u_values.sort()
                fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
                ax1.plot(s_values)
                ax1.set_title('Singleplayer Time')
                ax2.plot(m_values)
                ax2.set_title('Multiplayer Time')
                ax3.plot(u_values)
                ax3.set_title('Simulation Time')
                plt.show()
                s_mean = mean(s_values)
                print(f"The mean time for singleplayer is {round(s_mean, 1)} seconds")
                m_mean = mean(m_values)
                print(f"The mean time for multiplayer is {round(m_mean, 1)} seconds")
                u_mean = mean(u_values)
                print(f"The mean time for simulation is {round(u_mean, 1)} seconds")
    screen.fill((0, 0, 0))
    screen.blit(start_text, start_text_rect)
    pygame.draw.rect(screen, (0, 0, 0), singleplayer_button)
    pygame.draw.rect(screen, (0, 0, 0), multiplayer_button)
    pygame.draw.rect(screen, (0, 0, 0), simulation_button)
    pygame.draw.rect(screen, (0, 0, 0), quit_button)
    pygame.draw.rect(screen, (0, 0, 0), stat_button)
    screen.blit(singleplayer_text, (350, 215))
    screen.blit(multiplayer_text, (350, 290))
    screen.blit(simulation_text, (350, 365))
    screen.blit(quit_text, (15, 460))
    screen.blit(stat_text, (800, 460))
    player_two = pygame.Rect(size[0] - 60, size[1]/1 - 100, 50, 50)
    pygame.display.flip()
    while main_run:
        elapsed_time = time.time() - start_time
        score = int(elapsed_time)
        score_text = start_font.render(f"Time: {score}", True, (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_run = False
                start_menu = False
        keys = pygame.key.get_pressed()

        if multiplayer:
            # W controller
            if keys[pygame.K_w]:
                if not w_pressed:
                    w_pressed = True
                    if on_bottom_boundary:
                        vy = -15
            else:
                w_pressed = False
            # S Controller
            if keys[pygame.K_s]:
                s_pressed = True
            else:
                s_pressed = False
            if s_pressed:
                vy += gravity * 4
            else:
                vy += gravity
            # Right Controller
            if keys[pygame.K_RIGHT]:
                if not right_pressed:
                    right_pressed = True
                    if on_left_boundary:
                        vx = dvx
            else:
                right_pressed = False
            # Left Controller
            if keys[pygame.K_LEFT]:
                if not left_pressed:
                    left_pressed = True
                    if on_right_boundary:
                        vx = -dvx
            else:
                left_pressed = False
    # Singleplayer
        if singleplayer:
            # W controller
            if keys[pygame.K_w]:
                if not w_pressed:
                    w_pressed = True
                    if on_bottom_boundary:
                        vy = -15
            else:
                w_pressed = False
            # S Controller
            if keys[pygame.K_s]:
                s_pressed = True
            else:
                s_pressed = False
            # Right Controller
            random_number = random.randint(0,10)
            if random_number == 1:
                if not right_pressed:
                    right_pressed = True
                    if on_left_boundary:
                        vx = dvx
            else:
                right_pressed = False
            # Left Controller
            if random_number == 0:
                if not left_pressed:
                    left_pressed = True
                    if on_right_boundary:
                        vx = -dvx
            else:
                left_pressed = False
            if s_pressed:
                vy += gravity * 4
            else:
                vy += gravity
    # Simulation
        if simulation:
            # W controller
            random_number = random.randint(0,10)
            if random_number == 2:
                if not w_pressed:
                    w_pressed = True
                    if on_bottom_boundary:
                        vy = -15
            else:
                w_pressed = False
            # S Controller
            if keys[pygame.K_s]:
                s_pressed = True
            else:
                s_pressed = False
            # Right Controller
            if random_number == 1:
                if not right_pressed:
                    right_pressed = True
                    if on_left_boundary:
                        vx = dvx
            else:
                right_pressed = False
            # Left Controller
            if random_number == 0:
                if not left_pressed:
                    left_pressed = True
                    if on_right_boundary:
                        vx = -dvx
            else:
                left_pressed = False
            vy += gravity
        # Jumping/Falling
        player_one.y += vy
        # Left/Right
        player_two.x += vx
        
        # Boundries Player 1
        if player_one.top <= top_boundary:
            player_one.top = top_boundary
            vy = 0
        if player_one.bottom >= bottom_boundary:
            player_one.bottom = bottom_boundary
            vy = 0
            on_bottom_boundary = True
        else:
            on_bottom_boundary = False
        # Boundries Player 2
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
        if on_bottom_boundary:
            p1_rightpos = player_one.right
        else:
            
            p1_rightpos = 2000
        if player_two.right - 5 == p1_rightpos:
            game_over = True
            if singleplayer:
                fa(sfile, f"s{score}, ")
            if multiplayer:
                fa(sfile, f"m{score}, ")
            if simulation:
                fa(sfile, f"u{score}, ")
            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        main_run = False
                        game_over = False
                        start_menu = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(pygame.mouse.get_pos()):
                            player_two = pygame.Rect(size[0] - 60, size[1]/1 - 100, 50, 50)
                            start_time = time.time()
                            game_over = False
                        elif exit_button.collidepoint(pygame.mouse.get_pos()):
                            main_run = False
                            game_over = False
                screen.fill((0, 0, 0))
                screen.blit(text, text_rect)
                pygame.draw.rect(screen, (0, 0, 0), restart_button)
                pygame.draw.rect(screen, (0, 0, 0), exit_button)
                screen.blit(restart_text, restart_button)
                screen.blit(exit_text, exit_button)
                pygame.display.update()

        screen.blit(background_image, [0, 0])
        pygame.draw.rect(screen, (255, 0, 0), player_one)
        pygame.draw.rect(screen, (0, 0, 255), player_two)
        screen.blit(score_text, (780, 10))
        pygame.display.flip()
        clock.tick(fps)
pygame.quit()
