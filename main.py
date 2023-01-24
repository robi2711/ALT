import pygame

# Set up the pygame window
pygame.init()
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the board
board = []
for i in range(8):
    board.append([])
    for j in range(8):
        if (i + j) % 2 == 0:
            board[i].append(RED)
        else:
            board[i].append(GREEN)

# Set up the checkers
checkers = []
for i in range(3):
    for j in range(8):
        if (i + j) % 2 == 1:
            checkers.append((i, j, WHITE))

for i in range(5, 8):
    for j in range(8):
        if (i + j) % 2 == 1:
            checkers.append((i, j, BLACK))

# Set up the game state
selected_checker = None
current_player = BLACK
game_over = False

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            column = mouse_x // 50
            row = mouse_y // 50
            checker_index = None
            for i, (r, c, color) in enumerate(checkers):
                if r == row and c == column:
                    checker_index = i
                    break
            if checker_index is not None:
                if checkers[checker_index][2] == current_player:
                    selected_checker = checker_index
                else:
                    selected_checker = None
