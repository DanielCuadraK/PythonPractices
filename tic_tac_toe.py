from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(0,3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   "+board[i][0]+"   |   "+board[i][1]+"   |   "+board[i][2]+"   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    try:
        while True:
            move = int(input("Enter move: "))
            real_move = ()
            if type(move) == int and move >0 and move < 10:
                if move > 0 and move < 4:
                    real_move = (0, move-1)
                elif move > 3 and move < 7:
                    real_move = (1, move-4)
                elif move > 6 and move < 10:
                    real_move = (2, move-7)
                if real_move in free_fields:
                    board[real_move[0]][real_move[1]] = "X"
                    break
            print("Slot is not free")
    except:
        print("Enter a valid move")
            
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    free_fields.clear()
    for i in range (3):
        for j in range(3):
            if board[i][j] != "O" and board[i][j] != "X":
                free_fields.append((i,j))
    return free_fields
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or \
        (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or \
        (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or \
        (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or \
        (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or \
        (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or \
        (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
        (board[0][2] == sign and board[1][1] == sign and board[0][2] == sign):
        print("Victory for: ", sign)
        return True
    else:
        return False
            
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    while True:
        move = randrange(10)
        real_move = ()
        if move > 0 and move < 4:
            real_move = (0, move-1)
        elif move > 3 and move < 7:
            real_move = (1, move-4)
        elif move > 6 and move < 10:
            real_move = (2, move-7)
        if real_move in free_fields:
            board[real_move[0]][real_move[1]] = "O"
            break
    # The function draws the computer's move and updates the board.


#board = [["X" for i in range(3)] for j in range(3)]
board = [["1","2","3"],["4","O","6"],["7","8","9"]]
free_fields = []
display_board(board)
free_fields = make_list_of_free_fields(board)

while True:
    enter_move(board)
    free_fields = make_list_of_free_fields(board)
    if len(free_fields) == 0:
        print("No available slots")
        break
    display_board(board)
    if victory_for(board, "X"):
        print("end")
        break
    draw_move(board)
    free_fields = make_list_of_free_fields(board)
    if len(free_fields) == 0:
        print("No available slots")
        break
    display_board(board)
    if victory_for(board, "O"):
        print("end")
        break
