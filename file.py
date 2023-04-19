def print_board(board):
    print("-------------")
    print("| " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]) + " |")
    print("-------------")
    print("| " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]) + " |")
    print("-------------")
    print("| " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + " |")
    print("-------------")

def get_move(player, board):
    valid_move = False
    while not valid_move:
        move = input("Player " + str(player) + ", enter a valid move (0-8): ")
        if move.isdigit():
            move = int(move)
            if move >= 0 and move <= 8 and board[move] == "-":
                valid_move = True
    return move

def check_win(board):
    if board[0] == board[1] == board[2] != "-":
        return board[0]
    elif board[3] == board[4] == board[5] != "-":
        return board[3]
    elif board[6] == board[7] == board[8] != "-":
        return board[6]
    elif board[0] == board[3] == board[6] != "-":
        return board[0]
    elif board[1] == board[4] == board[7] != "-":
        return board[1]
    elif board[2] == board[5] == board[8] != "-":
        return board[2]
    elif board[0] == board[4] == board[8] != "-":
        return board[0]
    elif board[2] == board[4] == board[6] != "-":
        return board[2]
    else:
        return "-"

def tic_tac_toe():
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    print_board(board)
    player = "X"
    while True:
        move = get_move(player, board)
        board[move] = player
        print_board(board)
        winner = check_win(board)
        if winner != "-":
            print("Player " + winner + " wins!")
            break
        if "-" not in board:
            print("Tie game.")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"

tic_tac_toe()
