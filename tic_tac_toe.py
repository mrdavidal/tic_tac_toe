#rom random import randrange
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
    try:
        move = int(input("Enter your move:"))
    except: print("You havent't entered a valid move")
    if move > 0 and move < 10:
        move = str(move)
    else: print("You haven't entered a valid move")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if move == str(board[i][j]):
                del board[i][j]
                board[i].insert(j, "0")
    return board

display_board(board)
display_board(enter_move(board))
#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


#def draw_move(board):
    # The function draws the computer's move and updates the board.
