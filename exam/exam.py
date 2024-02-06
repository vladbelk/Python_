def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
            (board[3] == player and board[4] == player and board[5] == player) or \
            (board[6] == player and board[7] == player and board[8] == player) or \
            (board[0] == player and board[3] == player and board[6] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[0] == player and board[4] == player and board[8] == player) or \
            (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def tic_tac_toe():
    board = [" " for i in range(9)]
    player = "X"
    while True:
        print_board(board)
        try:
            move = int(input(f"Гравець {player}, Ваш хід: "))
            if move < 1 or move > 9:
                print("Невірний хід. Введіть номер ходу від 1 до 9: ")
                continue
            if board[move - 1] != " ":
                print("Ця клітинка вже зайнята. Будь ласка виберіть іншу!")
                continue
            board[move - 1] = player
            if check_win(board, player):
                print_board(board)
                print(f"Гравець {player} переміг!")
                break
            if " " not in board:
                print_board(board)
                print("Нічия!")
                break
            player = "O" if player == "X" else "X"
        except ValueError:
            print("Невірний хід. Введіть номер ходу від 1 до 9: ")
            continue

tic_tac_toe()
