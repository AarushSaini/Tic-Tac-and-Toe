def custom_sum(a, b, c):
    return a + b + c

def print_board(x_state, o_state):
    """Displays the current state of the Tic-Tac-Toe board."""
    board = []
    for i in range(9):
        if x_state[i]:
            board.append('X')
        elif o_state[i]:
            board.append('O')
        else:
            board.append(str(i))
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print(f"---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(state):
    """Checks if a player has won the game."""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if custom_sum(state[combo[0]], state[combo[1]], state[combo[2]]) == 3:
            return True
    return False

def is_draw(x_state, o_state):
    """Checks if the game is a draw."""
    return sum(x_state) + sum(o_state) == 9

def get_valid_input(occupied):
    """Prompts the user for a valid move."""
    while True:
        try:
            value = int(input("Please enter a value (0-8): "))
            if value < 0 or value > 8:
                print("Invalid input. Please enter a number between 0 and 8.")
            elif occupied[value]:
                print("This position is already occupied. Choose another.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")

def play_game():
    """Main function to play the Tic-Tac-Toe game."""
    x_state = [0] * 9
    o_state = [0] * 9
    turn = 1  # 1 for X, 0 for O
    print("Welcome to Tic-Tac-Toe!\n")
    
    while True:
        print_board(x_state, o_state)
        if turn == 1:
            print("X's Turn")
        else:
            print("O's Turn")

        occupied = [x_state[i] or o_state[i] for i in range(9)]
        value = get_valid_input(occupied)

        if turn == 1:
            x_state[value] = 1
        else:
            o_state[value] = 1

        if check_win(x_state if turn == 1 else o_state):
            print_board(x_state, o_state)
            print(f"{'X' if turn == 1 else 'O'} wins the match!")
            break

        if is_draw(x_state, o_state):
            print_board(x_state, o_state)
            print("It's a draw!")
            break

        turn = 1 - turn  # Switch turns

    if input("Do you want to play again? (yes/no): ").lower() == 'yes':
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    play_game()
