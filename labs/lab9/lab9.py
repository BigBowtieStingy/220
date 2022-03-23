"""
Alex James
lab9.py
Problem: Create a game of tic-tac-toe using functions and decision statements.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build_board():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_legal (board, position):
    position = eval(position)
    if board[position - 1] == "x" or board[position - 1] == "o":
        return False
    return True


def fill_spot (board, position, shape):
    shape = shape.strip()
    shape = shape.lower()
    position = eval(position)
    board[position - 1] = shape


def game_is_won(board):
    game_won_bool = False
    # Iterate through each possible solution, checking if all positions are the same shape
    winning_solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for solution in winning_solutions:
        location_one = board[solution[0] - 1]
        location_two = board[solution[1] - 1]
        location_three = board[solution[2] - 1]
        if location_one == location_two == location_three:
            game_won_bool = True
    return game_won_bool


def game_over(board):
    game_won_bool = game_is_won(board)
    no_moves_bool = True
    # If there is any space still with a number on the board, there must still be a move left.
    for space in board:
        space = str(space)
        if space.isnumeric():
            no_moves_bool = False
    game_over_bool = no_moves_bool or game_won_bool
    return game_over_bool


def get_winner(board):
    x_count = 0
    o_count = 0
    for space in board:
        if space == "x":
            x_count += 1
        elif space == "o":
            o_count += 1
    if x_count > o_count:
        return "X"
    elif o_count == x_count:
        return "O"


def draw_board(board, error_message):
    for i in range(3):
        index = i * 3
        print(" {} | {} | {} ".format(board[0 + index], board[1 + index], board[2 + index]))
        if i < 2:
            print(" --------- ")
    print(error_message)


def play(board):
    print("Welcome to Tic Tac Toe")
    print("Instructions: When prompted, the appropriate player should enter their move as the position")
    print("on the board where they wish to move. X will go first. \n")
    ans = "y"
    while ans[0] == "y":
        game_over_bool = False
        current_player = "X"
        error_message = ""
        while not game_over_bool:
            # Draw Board spaces:
            draw_board(board, error_message)
            position = input("Choose a position {}'s.".format(current_player))
            position.strip()
            if position.isnumeric() and is_legal(board, position):
                fill_spot(board, position, current_player)
                if current_player == "X":
                    current_player = "O"
                elif current_player == "O":
                    current_player = "X"
                error_message = ""
            else:
                error_message = "Space is filled or number is invalid. Try again."
            game_over_bool = game_over(board)
            winner_string = "No one won. A tie."
            if game_is_won(board):
                winner_string = get_winner(board)
                draw_board(board, error_message)
                print(winner_string + " won!")
            elif game_over_bool:
                draw_board(board, error_message)
                print(winner_string)
        ans = input("Want to play again?")
        ans = ans.lower()
        board = build_board()


play(build_board())