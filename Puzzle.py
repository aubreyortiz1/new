import random

# Initialize the game board
def initialize_board():
    board = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, '']]
    return board

# Print the current state of the board
def print_board(board):
    for row in board:
        print(" ".join(str(tile).rjust(2) for tile in row))
    print()

# Find the coordinates of the empty space
def find_empty_space(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == '':
                return i, j

# Check if the puzzle is solved
def is_solved(board):
    num = 1
    for i in range(4):
        for j in range(4):
            if i == 3 and j == 3:
                return True
            if board[i][j] != num:
                return False
            num += 1

# Slide a tile into the empty space
def slide_tile(board, row, col):
    empty_row, empty_col = find_empty_space(board)
    if (abs(row - empty_row) == 1 and col == empty_col) or \
       (abs(col - empty_col) == 1 and row == empty_row):
        board[empty_row][empty_col], board[row][col] = board[row][col], board[empty_row][empty_col]
        return True
    return False

# Shuffle the board to start the game
def shuffle_board(board, moves=100):
    for _ in range(moves):
        empty_row, empty_col = find_empty_space(board)
        possible_moves = []
        if empty_row > 0:
            possible_moves.append((empty_row - 1, empty_col))
        if empty_row < 3:
            possible_moves.append((empty_row + 1, empty_col))
        if empty_col > 0:
            possible_moves.append((empty_row, empty_col - 1))
        if empty_col < 3:
            possible_moves.append((empty_row, empty_col + 1))
        row, col = random.choice(possible_moves)
        slide_tile(board, row, col)

# Main game loop
def play_game():
    board = initialize_board()
    shuffle_board(board)
    
    while not is_solved(board):
        print_board(board)
        move = input("Enter the row and column of the tile you want to move (e.g., '2 3'): ")
        row, col = map(int, move.split())
        
        if row < 1 or row > 4 or col < 1 or col > 4:
            print("Invalid move! Row and column must be between 1 and 4.")
            continue
        
        if not slide_tile(board, row - 1, col - 1):
            print("Invalid move! You can only slide tiles into the empty space.")
        
    print("Congratulations! You solved the puzzle!")

# Start the game
play_game()
