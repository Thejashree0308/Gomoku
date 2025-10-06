import pygame, sys

GRID_SIZE = 15
CELL_SIZE = 40
MARGIN = 2
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
FPS = 60

WHITE = (245, 245, 245)
BG = (30, 30, 40)
PLAYER_COLOR = (50, 200, 50)
AI_COLOR = (200, 50, 50)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gomoku: Player vs AI")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def draw_board():
    screen.fill(BG)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col*CELL_SIZE + MARGIN, row*CELL_SIZE + MARGIN,
                               CELL_SIZE - 2*MARGIN, CELL_SIZE - 2*MARGIN)
            pygame.draw.rect(screen, WHITE, rect)
            if board[row][col] == 1:
                pygame.draw.circle(screen, PLAYER_COLOR, rect.center, CELL_SIZE//2 - 4)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, AI_COLOR, rect.center, CELL_SIZE//2 - 4)

def check_win(player):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if c <= GRID_SIZE-5 and all(board[r][c+i]==player for i in range(5)):
                return True
            if r <= GRID_SIZE-5 and all(board[r+i][c]==player for i in range(5)):
                return True
            if r <= GRID_SIZE-5 and c <= GRID_SIZE-5 and all(board[r+i][c+i]==player for i in range(5)):
                return True
            if r >= 4 and c <= GRID_SIZE-5 and all(board[r-i][c+i]==player for i in range(5)):
                return True
    return False

def ai_move():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c] == 0:
                board[r][c] = 2
                if check_win(2):
                    return
                board[r][c] = 1
                if check_win(1):
                    board[r][c] = 2
                    return
                board[r][c] = 0
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c] == 0:
                board[r][c] = 2
                return

player_turn = True
game_over = False
winner_text = ""

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and player_turn:
            mx, my = pygame.mouse.get_pos()
            col = mx // CELL_SIZE
            row = my // CELL_SIZE
            if board[row][col] == 0:
                board[row][col] = 1
                if check_win(1):
                    winner_text = "Player Wins!"
                    game_over = True
                player_turn = False

    if not player_turn and not game_over:
        ai_move()
        if check_win(2):
            winner_text = "AI Wins!"
            game_over = True
        player_turn = True

    screen.fill(BG)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col*CELL_SIZE + MARGIN, row*CELL_SIZE + MARGIN,
                               CELL_SIZE - 2*MARGIN, CELL_SIZE - 2*MARGIN)
            pygame.draw.rect(screen, WHITE, rect)
            if board[row][col] == 1:
                pygame.draw.circle(screen, PLAYER_COLOR, rect.center, CELL_SIZE//2 - 4)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, AI_COLOR, rect.center, CELL_SIZE//2 - 4)

    if game_over:
        text = font.render(winner_text, True, (255, 215, 0))
        screen.blit(text, ((WIDTH-text.get_width())//2, (HEIGHT-text.get_height())//2))

    pygame.display.flip()
