def check_removal(board):
    n = len(board)
    removal_happened = False
    i = 0
    while i < n:
        if board[i] != '_':
            j = i + 1
            while j < n and board[j] == board[i]:
                j += 1
            if (j - i) >= 3:
                for k in range(i, j):
                    board[k] = '_'
                removal_happened = True
            i = j
        else:
            i += 1
    return removal_happened


def print_board(board):
    print(" ".join(board))


def main():
    n = int(input().strip())
    board = ['_'] * n

    ai_score = 0
    user_score = 0
    turn = 0

    ai_colors = ['R', 'B', 'R', 'G']
    ai_move_count = 0

    while '_' in board:
        if turn == 0:
            if ai_move_count == 0:
                pos = n // 2
            else:
                pos = board.index('_')
            color = ai_colors[ai_move_count % len(ai_colors)]
            ai_move_count += 1

            board[pos] = color
            print(f"AI step {pos} {color}")
            print_board(board)

            if check_removal(board):
                ai_score += 1
                print_board(board)
            turn = 1

        else:
            valid_move = False
            while not valid_move:
                try:
                    parts = input().split()
                except EOFError:
                    continue
                if len(parts) < 2:
                    continue
                try:
                    pos = int(parts[0])
                    color = parts[1]
                except ValueError:
                    continue
                if not (0 <= pos < n) or board[pos] != '_':
                    print("This place is taken.")
                    continue
                valid_move = True

            board[pos] = color
            print(f"Your step {pos} {color}")
            print_board(board)
            if check_removal(board):
                user_score += 1
                print_board(board)
            turn = 0

    if ai_score > user_score:
        print(f"AI win! {ai_score} : {user_score}")
    elif user_score > ai_score:
        print(f"You win! {user_score} : {ai_score}")
    else:
        print("We have a tie.")


if __name__ == "__main__":
    main()
