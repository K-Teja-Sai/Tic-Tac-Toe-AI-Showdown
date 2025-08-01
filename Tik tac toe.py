import math

def print_board(board): 
    for row in board: 
        print(" | ".join(row)) 
        print("-" * 9) 

def check_winner(board): 
    for row in board: 
        if row[0] == row[1] == row[2] != " ": 
            return row[0] 
    for col in range(3): 
        if board[0][col] == board[1][col] == board[2][col] != " ": 
            return board[0][col] 
    if board[0][0] == board[1][1] == board[2][2] != " ": 
        return board[0][0] 
    if board[0][2] == board[1][1] == board[2][0] != " ": 
        return board[0][2] 
    return None 

def is_board_full(board): 
    return all(cell != " " for row in board for cell in row) 

def player_move(board): 
    while True: 
        try: 
            move = int(input("Enter your move (1-9): ")) - 1 
            row, col = divmod(move, 3) 
            if board[row][col] == " ": 
                board[row][col] = "X" 
                break 
            else: 
                print("Cell already taken. Try again.") 
        except (ValueError, IndexError): 
            print("Invalid input. Please enter a number between 1 and 9.") 

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O": 
        return 10 - depth
    elif winner == "X":  
        return depth - 10
    elif is_board_full(board): 
        return 0  

    if is_maximizing:  # Computer's turn
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(best_score, score)
        return best_score
    else:  # Player's turn
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(best_score, score)
        return best_score

def computer_move(board): 
    best_score = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move:
        row, col = best_move
        board[row][col] = "O"

def play_game(): 
    board = [[" " for _ in range(3)] for _ in range(3)] 
    print("Welcome to Tic-Tac-Toe!") 

    while True: 
        print_board(board) 
        player_move(board) 
        if check_winner(board) == "X": 
            print_board(board) 
            print("You win!") 
            break 
        if is_board_full(board): 
            print_board(board) 
            print("It's a tie!") 
            break 

        computer_move(board) 
        if check_winner(board) == "O": 
            print_board(board) 
            print("Computer wins!") 
            break 
        if is_board_full(board): 
            print_board(board) 
            print("It's a tie!") 
            break 

if __name__ == "__main__": 
    play_game()