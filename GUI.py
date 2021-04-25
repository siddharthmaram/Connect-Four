from game_functions import *
import sys, pygame
from window import *


pygame.init()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
image = pygame.image.load("square.png")
yellow_coin = pygame.image.load("yellow.png")
red_coin = pygame.image.load("red.png")
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 32)
text_display = font.render("Welcome to CONNECT FOUR", True, green, white)
textRect = text_display.get_rect()
textRect.center = (400, 500)

color_light = (170, 170, 170)
color_dark = (100, 100, 100)

smallfont = pygame.font.SysFont('Corbel', 32)
text = smallfont.render('New Game', True, (255, 255, 255))

welcome_font = pygame.font.Font('freesansbold.ttf', 32)
welcome = font.render("Welcome to CONNECT FOUR Game!", True, green, black)


class Square:
    def __init__(self, row, col, is_filled):
        self.row = row
        self.col = col
        self.is_filled = is_filled

    def draw(self, cor_x, cor_y):
        screen.blit(image, (cor_x, cor_y))


class Coin(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.cor_x = x
        self.cor_y = y
        # self.move_x = move_x

    def draw(self):
        if self.color == "red":
            screen.blit(red_coin, (self.cor_x, self.cor_y))
        else:
            screen.blit(yellow_coin, (self.cor_x, self.cor_y))

    def update(self):
        pos = pygame.mouse.get_pos()
        if pos[0] in range(120, 465):
            self.cor_x = pos[0] - 20
        if self.color == "red":
            screen.blit(red_coin, (self.cor_x, self.cor_y))
        else:
            screen.blit(yellow_coin, (self.cor_x, self.cor_y))


def display_board(board):
    for i in range(6):
        for j in range(7):
            exec(f"square_{i}{j} = Square({j}, {i}, False)")
            exec(f"square_{i}{j}.draw(100 + 56*j, 100 + 59*i)")
            if board[i][j] != "O":
                exec(f"coin_{i}{j}.draw()")


def drop_coin(col, player, board):
    moves = possible_moves(board)
    if col in moves:
        for i in range(5, -1, -1):
            if board[i][col] == "O":
                row = i
                break
        execute_move(col, player, board)
        color = "yellow" if player == 'Y' else "red"
        exec(f"coin_{row}{col} = Coin('{color}', {101 + 56*col}, {103 + 59*row})", globals())
        exec(f"coin_{row}{col}.draw()")


def player_move(player, board):
    color = "yellow" if player == 'Y' else "red"
    moves = possible_moves(board)
    exec(f"temp_coin = Coin('{color}',100 , 48)", globals())
    moved = False
    while not moved:
        screen.fill((0, 0, 0))
        display_board(board)
        screen.blit(welcome, (25, 20))
        temp_coin.update()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(100, 156) and 0 in moves:
                    drop_coin(0, player, board)
                    moved = True
                    break
                elif pos[0] in range(156, 156 + 56) and 1 in moves:
                    drop_coin(1, player, board)
                    moved = True
                    break
                elif pos[0] in range(156, 156 + 56*2) and 2 in moves:
                    drop_coin(2, player, board)
                    moved = True
                    break
                elif pos[0] in range(156, 156 + 56*3) and 3 in moves:
                    drop_coin(3, player, board)
                    moved = True
                    break
                elif pos[0] in range(156, 156 + 56*4) and 4 in moves:
                    drop_coin(4, player, board)
                    moved = True
                    break
                elif pos[0] in range(156, 156 + 56*5) and 5 in moves:
                    drop_coin(5, player, board)
                    moved = True
                    break
                elif pos[0] in range(156, 156 + 56*6) and 6 in moves:
                    drop_coin(6, player, board)
                    moved = True
                    break
                else:
                    continue
            pygame.display.update()


def computer_move(computer, board):
    a = best_move(board, computer)
    drop_coin(a, computer, board)


def new_game(x, y):
    player1.set("")
    player2.set("")
    player1_color.set("")
    while not can_start():
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x <= mouse[0] <= x + 140 and y <= mouse[1] <= y + 30:
                    new_window()
                    break
        if can_start():
            break

        mouse = pygame.mouse.get_pos()

        if x <= mouse[0] <= x + 140 and y <= mouse[1] <= y + 30:
            pygame.draw.rect(screen, color_light, [x, y, 140, 30])

        else:
            pygame.draw.rect(screen, color_dark, [x, y, 140, 30])
        screen.blit(welcome, (25, 20))
        screen.blit(text, (x, y))
        pygame.display.update()
    return True


def one_player_game():
    global text_display
    board = [
            ["O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O"],
        ]
    if player1.get() == "Human":
        human = "Y" if player1_color.get() == "Yellow" else "R"
        computer = "R" if human == "Y" else "Y"
    else:
        computer = "Y" if player1_color.get() == "Yellow" else "R"
        human = "R" if computer == "Y" else "Y"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(welcome, (25, 20))
        display_board(board)
        player_move(human, board)
        pygame.display.update()
        if check_win(board, human):
            screen.fill((0, 0, 0))
            display_board(board)
            screen.blit(welcome, (25, 20))
            text_display = font.render("You Won!", True, green, black)
            screen.blit(text_display, textRect)
            pygame.display.update()
            pygame.time.wait(2000)
            break
        elif not possible_moves(board):
            screen.fill((0, 0, 0))
            display_board(board)
            screen.blit(welcome, (25, 20))
            text_display = font.render("Draw Match", True, green, black)
            screen.blit(text_display, textRect)
            pygame.display.update()
            pygame.time.wait(2000)
            break
        computer_move(computer, board)
        pygame.display.update()
        if check_win(board, computer):
            text_display = font.render("Computer Wins!", True, green, black)
            screen.fill((0, 0, 0))
            display_board(board)
            screen.blit(welcome, (25, 20))
            screen.blit(text_display, textRect)
            pygame.display.update()
            pygame.time.wait(2000)
            break
        elif not possible_moves(board):
            screen.fill((0, 0, 0))
            display_board(board)
            screen.blit(welcome, (25, 20))
            text_display = font.render("Draw Match", True, green, black)
            screen.blit(text_display, textRect)
            pygame.display.update()
            pygame.time.wait(2000)
            break
        pygame.time.wait(200)


def two_player_game():
    global text_display
    board = [
            ["O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O"],
        ]
    player_1 = "Y" if player1_color.get() == "Yellow" else "R"
    player_2 = "R" if player_1 == "Y" else "Y"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(welcome, (25, 20))
        display_board(board)
        player_move(player_1, board)
        pygame.display.update()
        if check_win(board, player_1):
            screen.fill((0, 0, 0))
            screen.blit(welcome, (25, 20))
            display_board(board)
            text_display = font.render("Player1 Won!", True, green, black)
            screen.blit(text_display, textRect)
            pygame.display.update()
            pygame.time.wait(2000)
            break
        elif not possible_moves(board):
            screen.fill((0, 0, 0))
            display_board(board)
            screen.blit(welcome, (25, 20))
            text_display = font.render("Draw Match", True, green, black)
            screen.blit(text_display, textRect)
            pygame.display.update()
            pygame.time.wait(2000)
            break
        pygame.time.wait(500)
        player_move(player_2, board)
        pygame.display.update()
        if check_win(board, player_2):
            text_display = font.render("Player2 Wins!", True, green, black)
            screen.fill((0, 0, 0))
            screen.blit(welcome, (25, 20))
            display_board(board)
            screen.blit(text_display, textRect)
            pygame.display.update()
            pygame.time.wait(2000)
            break
        elif not possible_moves(board):
            screen.fill((0, 0, 0))
            screen.blit(welcome, (25, 20))
            display_board(board)
            text_display = font.render("Draw Match", True, green, black)
            screen.blit(text_display, textRect)
            pygame.display.update()
            pygame.time.wait(2000)
            break


