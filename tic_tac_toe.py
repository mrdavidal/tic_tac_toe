import random
from random import randrange
counter = 0
board = [[row for row in range(3)]for collumn in range(3)]

for i in range(len(board)):
    for j in range(len(board[i])):
        board[i][j] = counter + 1
        counter += 1
for i in range(len(board)):
    for j in range(len(board[i])):
        board[i][j] = str(board[i][j])

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    nr1 = "1"
    nr2 = "2"
    nr3 = "3"
    nr4 = "4"
    nr5 = "5"
    nr6 = "6"
    nr7 = "7"
    nr8 = "8"
    nr9 = "9"
    up = "-------"
    side = "|       "
    check = -1
    check2 = -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "x" or board[i][j] == "0":
                check = i
                check2 = j
            if check > -1 and check2 > -1:
                if check == 0 and check2 == 0:
                    nr1 = board[i][j]
                elif check == 0 and check2 == 1:
                    nr2 = board[i][j]
                elif check == 0 and check2 == 2:
                    nr3 = board[i][j]
                elif check == 1 and check2 == 0:
                    nr4 = board[i][j]
                elif check == 1 and check2 == 1:
                    nr5 = board[i][j]
                elif check == 1 and check2 == 2:
                    nr6 = board[i][j]
                elif check == 2 and check2 == 0:
                    nr7 = board[i][j]
                elif check == 2 and check2 == 1:
                    nr8 = board[i][j]
                elif check == 2 and check2 == 2:
                    nr9 = board[i][j]
                check = -1
                check2 = -1

    side_midle1 = "|   " + nr1 + "   "
    side_midle2 = "|   " + nr2 + "   "
    side_midle3 = "|   " + nr3 + "   "
    side_midle4 = "|   " + nr4 + "   "
    side_midle5 = "|   " + nr5 + "   "
    side_midle6 = "|   " + nr6 + "   "
    side_midle7 = "|   " + nr7 + "   "
    side_midle8 = "|   " + nr8 + "   "
    side_midle9 = "|   " + nr9 + "   "
    print("+-------", up, up, sep="+",end="+\n")
    print(side * 4)
    print(side_midle1 + side_midle2 + side_midle3)
    print(side * 4)
    print("+-------", up, up, sep="+",end="+\n")
    print(side * 4)
    print(side_midle4 + side_midle5 + side_midle6)
    print(side * 4)
    print("+-------", up, up, sep="+",end="+\n")
    print(side * 4)
    print(side_midle7 + side_midle8 + side_midle9)
    print(side * 4)
    print("+-------", up, up, sep="+",end="+\n")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    enter = input("Enter your move:")
    try:
        move = int(enter)
    except:
        print("You havent't entered a valid move")
    if move > 0 and move < 10:
        move = str(move)
    else: print("You haven't entered a valid move")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if move == str(board[i][j]):
                del board[i][j]
                board[i].insert(j, "0")
    return board

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_field = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "x" or board[i][j] == "0":
                continue
            else:
                row_collumn = i, j
                free_field.append(row_collumn)
    return free_field

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == 0 and board[i][j] == sign and board[i][j + 1] == sign and board[i][j + 2] == sign:
                return 1
            elif i == 0 and board[i][j] == sign and board[i + 1][j] == sign and board[i + 2][j] == sign:
                return 1
            elif i == 0 and j == 0 and board[i][j] == sign and board[i + 1][j + 1] == sign and board[i + 2][j + 2] == sign:
                return 1
            elif i == 0 and j == 0 and board[i][j + 2] == sign and board[i + 1][j + 1] == sign and board[i + 2][j] == sign:
                return 1
    return 0

def draw_move(board):
    # The function draws the computer's move and updates the board.
    nr = random.randrange(1,10)
    counter = 1
    t_board = make_list_of_free_fields(board)
    if len(t_board) == 9:
        board[1][1] = "x"
        return board
    else:
        while counter > 0:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == str(nr):
                        del board[i][j]
                        board[i].insert(j, "x")
                        counter = 0
            nr = random.randrange(1,10)

    return board
display_board(draw_move(board))
while victory_for(board, "0") == 0 and victory_for(board, "x") == 0:
    if victory_for(board, "0") == 0 and victory_for(board, "x") == 0:
        if len(make_list_of_free_fields(board)) < 1:
            break
        display_board(enter_move(board))
    if victory_for(board, "0") == 0 and victory_for(board, "x") == 0:
        display_board(draw_move(board))
