import time
board1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
board2 = [
    [2, 0, 0, 0, 8, 0, 3, 0, 0],
    [0, 6, 0, 0, 7, 0, 0, 8, 4],
    [0, 3, 0, 5, 0, 0, 2, 0, 9],

    [0, 0, 0, 1, 0, 5, 4, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 2, 7, 0, 6, 0, 0, 0],

    [3, 0, 1, 0, 0, 7, 0, 4, 0],
    [7, 2, 0, 0, 4, 0, 0, 6, 0],
    [0, 0, 4, 0, 1, 0, 0, 0, 3]
]
board3 = [
    [0, 0, 0, 9, 0, 0, 0, 0, 7],
    [0, 5, 0, 0, 1, 0, 0, 9, 0],
    [2, 0, 0, 5, 0, 4, 0, 0, 0],

    [0, 0, 0, 7, 0, 0, 0, 8, 0],
    [1, 6, 0, 0, 0, 0, 0, 4, 9],
    [0, 3, 0, 0, 0, 1, 0, 0, 0],

    [0, 0, 0, 3, 0, 6, 0, 0, 1],
    [0, 7, 0, 0, 8, 0, 0, 6, 0],
    [6, 0, 0, 0, 0, 2, 0, 0, 0]
]

# Define multiple puzzles
puzzles = [board1, board2, board3]  # Use the boards from above

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            val = board[i][j]
            print(val if val != 0 else ".", end=" ")
        print()

def find_empty_position(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, position, number):
    row, col = position

    # Check row
    if number in board[row]:
        return False

    # Check column
    if number in [board[i][col] for i in range(9)]:
        return False

    # Check box
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number:
                return False

    return True

def solve_board(board):
    empty = find_empty_position(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, (row, col), num):
            board[row][col] = num
            if solve_board(board):
                return True
            board[row][col] = 0

    return False

# Solve all hardcoded puzzles
total_start = time.time()
for i, board in enumerate(puzzles):
    print(f"\nPuzzle {i + 1} (Before):")
    print_board(board)
    start_time = time.time()
    if solve_board(board):
        end_time = time.time()
        print(f"\nPuzzle {i + 1} (Solved in {round(end_time - start_time, 4)}s):")
        print_board(board)
    else:
        print("No solution found.")
total_end = time.time()

print(f"\nTotal Time for all puzzles: {round(total_end - total_start, 4)} seconds")
