import pygame
pygame.font.init()

WIDTH, HEIGHT = 900, 900
COL_WIDTH, ROW_HEIGHT = WIDTH // 3, HEIGHT // 3
ROWS = 3
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 100, 100)
GREY = (35, 35, 35)
GOLD = (249, 166, 3)

WINNER_FONT = pygame.font.SysFont('comicsans', 100)
X_FONT = pygame.font.SysFont('trebuchetms', 300)

FPS = 60

GAME_GRID = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

def draw_window(win, grid):
    win.fill(GREY)
    make_grid(win, grid)

    pygame.mouse.set_visible(True)
    pygame.display.update()

def make_grid(win, grid): 
    distance_between_rows = WIDTH // ROWS
    x, y = 0, 0

    for l in range(ROWS):
        x += distance_between_rows
        y += distance_between_rows
        pygame.draw.line(win, GOLD, (x, 0), (x, HEIGHT))
        pygame.draw.line(win, GOLD, (0, y), (HEIGHT, y))

def handle_mouse_click(win, grid, clicked, x_player, o_player):
    if x_player:
        x_player = not x_player
        o_player = not o_player
    elif o_player:
        x_player = not x_player
        o_player = not o_player

    for r in range(ROWS):
        for c in range(ROWS):
            if grid[r][c] == 'x':
                draw_x(win, (r, c))
            elif grid[r][c] == 'o':
                draw_circle(win, (r, c))

    check_winner(win, grid)
    check_draw(win, grid)
    clicked = False
    return clicked, x_player, o_player
               
def draw_circle(win, position):
    if position[0] == 0 and position[1] == 0:
        pygame.draw.circle(win, RED, (COL_WIDTH // 2, COL_WIDTH // 2), 135, 1)
    elif position[0] == 0 and position[1] == 1:
        pygame.draw.circle(win, RED, (COL_WIDTH * 1.5, COL_WIDTH // 2), 135, 1)
    elif position[0] == 0 and position[1] == 2:
        pygame.draw.circle(win, RED, (COL_WIDTH * 2.5, COL_WIDTH // 2), 135, 1)
    elif position[0] == 1 and position[1] == 0:
        pygame.draw.circle(win, RED, (COL_WIDTH // 2, COL_WIDTH * 1.5), 135, 1)
    elif position[0] == 1 and position[1] == 1:
        pygame.draw.circle(win, RED, (COL_WIDTH * 1.5, COL_WIDTH * 1.5), 135, 1)
    elif position[0] == 1 and position[1] == 2:
        pygame.draw.circle(win, RED, (COL_WIDTH * 2.5, COL_WIDTH * 1.5), 135, 1)
    elif position[0] == 2 and position[1] == 0:
        pygame.draw.circle(win, RED, (COL_WIDTH // 2, COL_WIDTH * 2.5), 135, 1)
    elif position[0] == 2 and position[1] == 1:
        pygame.draw.circle(win, RED, (COL_WIDTH * 1.5, COL_WIDTH * 2.5), 135, 1)
    elif position[0] == 2 and position[1] == 2:
        pygame.draw.circle(win, RED, (COL_WIDTH * 2.5, COL_WIDTH * 2.5), 135, 1)
    pygame.display.update()

def draw_x(win, position):
    if position[0] == 0 and position[1] == 0:
        pygame.draw.aaline(win ,BLUE, (20, 20), (WIDTH // 3 - 20, HEIGHT // 3 - 20)) 
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 - 20, 20), (20, HEIGHT // 3 - 20)) 
    elif position[0] == 0 and position[1] == 1:
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 + 20, 20), (WIDTH // 3 + WIDTH // 3 - 20, HEIGHT // 3 - 20)) 
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 + WIDTH // 3 - 20, 20), (WIDTH // 3 + 20, HEIGHT // 3 - 20)) 
    elif position[0] == 0 and position[1] == 2:
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 * 2 + 20, 20), (WIDTH - 20, HEIGHT // 3 - 20))
        pygame.draw.aaline(win ,BLUE, (WIDTH - 20, 20), (WIDTH // 3 * 2 + 20, HEIGHT // 3 - 20)) 

    elif position[0] == 1 and position[1] == 0:
        pygame.draw.aaline(win ,BLUE, (20, HEIGHT // 3 + 20), (WIDTH // 3 - 20, HEIGHT // 3 * 2 - 20)) 
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 - 20, HEIGHT // 3 + 20), (20, HEIGHT // 3 * 2 - 20)) 
    elif position[0] == 1 and position[1] == 1:
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 + 20, HEIGHT // 3 + 20), (WIDTH // 3 * 2 - 20, HEIGHT // 3 * 2 - 20))  
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 * 2 - 20, HEIGHT // 3 + 20), (WIDTH // 3 + 20, HEIGHT // 3 * 2 - 20)) 
    elif position[0] == 1 and position[1] == 2:
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 * 2 + 20, HEIGHT // 3 + 20), (WIDTH - 20 ,HEIGHT // 3 * 2 - 20))  
        pygame.draw.aaline(win ,BLUE, (WIDTH - 20, HEIGHT // 3 + 20), (WIDTH // 3 * 2 + 20 ,HEIGHT // 3 * 2 - 20)) 

    elif position[0] == 2 and position[1] == 0:
        pygame.draw.aaline(win ,BLUE, (20, HEIGHT // 3 * 2 + 20), (WIDTH // 3 - 20, HEIGHT - 20))  
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 - 20, HEIGHT // 3 * 2 + 20), (20, HEIGHT - 20)) 
    elif position[0] == 2 and position[1] == 1:
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 + 20, HEIGHT // 3 * 2 + 20), (WIDTH // 3 * 2 - 20, HEIGHT - 20))  
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 * 2 - 20, HEIGHT // 3 * 2 + 20), (WIDTH // 3 + 20, HEIGHT - 20)) 
    elif position[0] == 2 and position[1] == 2:
        pygame.draw.aaline(win ,BLUE, (WIDTH // 3 * 2 + 20, HEIGHT // 3 * 2 + 20), (WIDTH - 20, HEIGHT - 20))  
        pygame.draw.aaline(win ,BLUE, (WIDTH - 20, HEIGHT // 3 * 2 + 20), (WIDTH // 3 * 2 + 20, HEIGHT - 20)) 
    
    pygame.display.update()

def check_winner(win, grid):
    for r in range(ROWS):
        #row wins
        if grid[r][0] == grid[r][1] == grid[r][2] != '':
            winner(win, grid[r][0])
        #column wins
        elif grid[0][r] == grid[1][r] == grid[2][r] != '':
            winner(win, grid[0][r])
    #diagonal 1 win
    if grid[0][0] == grid[1][1] == grid[2][2] != '':
        winner(win, grid[r][0])
    #diagonal 2 win
    if grid[0][2] == grid[1][1] == grid[2][0] != '':
        winner(win, grid[r][0])
    

def winner(win, player):
    if(player == 'draw'):
        winner_text = WINNER_FONT.render('Draw!', 1, WHITE)
    else:
        winner_text = WINNER_FONT.render(str(player) + ' wins!', 1, WHITE)
    win.blit(winner_text, (WIDTH//2 - winner_text.get_width()//2, HEIGHT//2 - winner_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()

def check_draw(win, grid):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == '':
                return False
    winner(win, 'draw')
    

def main():
    clock = pygame.time.Clock()
    run = True

    x_player, o_player = False, True
    clicked = False
    draw_window(WIN, GAME_GRID)

    start_text = WINNER_FONT.render('O player starts', 1, WHITE)
    WIN.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2 - start_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)

    draw_window(WIN, GAME_GRID)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and clicked == False:
                clicked = True
                x, y = pygame.mouse.get_pos()
                col = int(x // COL_WIDTH)
                row = int(y // ROW_HEIGHT)

                if GAME_GRID[row][col] == '': 
                    GAME_GRID[row][col] = 'o' if o_player else 'x'
                    clicked, x_player, o_player = handle_mouse_click(WIN, GAME_GRID, clicked, x_player, o_player)
        

    pygame.quit()
    
if __name__ == "__main__":
    main()
