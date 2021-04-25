# from random import choice
from os import system, name
from colorama import init
from colorama import Fore


init(autoreset=True)


def display_board(board):
    print("Welcome to CONNECT FOUR game!")
    print('+-------------+')
    print(' 1 2 3 4 5 6 7')
    for i in board:
        print("|", end="")
        for j in i:
            if j == "R":
                print(Fore.RED + f"{j}", end="")
                print("|", end="")
            elif j == "Y":
                print(Fore.YELLOW + f"{j}", end="")
                print("|", end="")
            else:
                print(f"{j}|", end="")
        print("\n", end="")
    print('+-------------+')


def possible_moves(board):
    cols = []
    for i in range(7):
        for j in board:
            if j[i] == "O":
                cols.append(i)
                break
    return cols


def execute_move(col, player, board):
    for j in board[::-1]:
        if j[col] == "O":
            j[col] = player
            break
    else:
        return 0


def computer_move(computer, board):
    a = best_move(board, computer)
    execute_move(a, computer, board)


def check_win(board, tile):
    boardHeight = len(board[0])
    boardWidth = len(board)

    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True

    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True

    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True

    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True

    return False


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def count_threes(board, tile):
    boardHeight = len(board[0])
    boardWidth = len(board)
    count = 0
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            a = [board[x][y], board[x + 1][y], board[x + 2][y], board[x + 3][y]]
            if a.count(tile) == 3 and a.count("O") == 1:
                count += 1

    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            b = [board[x][y], board[x][y + 1], board[x][y + 2], board[x][y + 3]]
            if b.count(tile) == 3 and b.count("O") == 1:
                count += 1

    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            c = [board[x][y], board[x + 1][y - 1], board[x + 2][y - 2], board[x + 3][y - 3]]
            if c.count(tile) == 3 and c.count("O") == 1:
                count += 1

    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            d = [board[x][y] , board[x + 1][y + 1] , board[x + 2][y + 2], board[x + 3][y + 3]]
            if d.count(tile) == 3 and d.count("O") == 1:
                count += 1

    return count


# def best_move(board, computer):
#     moves = possible_moves(board)
#     player = "R" if computer == "Y" else "Y"
#     m = (0, -10000)
#     for i in moves:
#         execute_move(i, computer, board)
#         points = 0
#         points += count_threes(board, computer)
#         points += count_threes(board, player)*(-100)
#         if check_win(board, computer):
#             points += 10**6
#         if points > m[1]:
#             m = (i, points)
#         for j in board:
#             if j[i] != "O":
#                 j[i] = "O"
#                 break
#     return m[0]


def is_terminal_node(board):
    if check_win(board, "R") or check_win(board, "Y"):
        return True
    return False


def evaluate_board(board, player):
    points = 0
    opp = "R" if player == "Y" else "Y"
    points += count_threes(board, player)
    points += count_threes(board, opp)*(-100)
    if check_win(board, player):
        points += 10**6
    if check_win(board, opp):
        points -= 10000
    return points


def minimax(board, depth, is_maximizing_player, player, opponent):
    if depth == 0 or is_terminal_node(board):
        return evaluate_board(board, player)
    if is_maximizing_player:
        value = -10**9
        for i in possible_moves(board):
            execute_move(i, player, board)
            value = max(value, minimax(board, depth-1, False, player, opponent))
            for j in board:
                if j[i] != "O":
                    j[i] = "O"
                    break
        return value
    else:
        value = 10**9
        for i in possible_moves(board):
            execute_move(i, opponent, board)
            value = min(value, minimax(board, depth - 1, True, player, opponent))
            for j in board:
                if j[i] != "O":
                    j[i] = "O"
                    break
        return value


def best_move(board, player):
    moves = possible_moves(board)
    opponent = "R" if player == "Y" else "Y"
    m = (0, -10**9)
    for i in moves:
        execute_move(i, player, board)
        v = minimax(board, 3, False, player, opponent)
        if v > m[1]:
            m = (i, v)
        for j in board:
            if j[i] != "O":
                j[i] = "O"
                break
    return m[0]









