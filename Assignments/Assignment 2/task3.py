

import time
from ortools.sat.python import cp_model
#read puzles
def read_puzzles(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if len(line.strip()) == 81]

puzzles = read_puzzles("sudoku_input.txt")

# ========== MY VERSION (AC3 + BACKTRACKING) ==========

# Peers Calculation (once)
def index(row, col):
    return row * 9 + col

def get_peers():
    peers = [[] for _ in range(81)]
    for i in range(9):
        for j in range(9):
            idx = index(i, j)
            row = [index(i, k) for k in range(9) if k != j]
            col = [index(k, j) for k in range(9) if k != i]
            block = [
                index(i//3*3 + m, j//3*3 + n)
                for m in range(3) for n in range(3)
                if index(i//3*3 + m, j//3*3 + n) != idx
            ]
            peers[idx] = list(set(row + col + block))
    return peers

peers = get_peers()

def ac3(domains):
    queue = [(xi, xj) for xi in range(81) for xj in peers[xi]]
    while queue:
        xi, xj = queue.pop(0)
        if revise(domains, xi, xj):
            if not domains[xi]:
                return False
            for xk in peers[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(domains, xi, xj):
    revised = False
    for x in domains[xi][:]:
        if all(x == y for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised

def backtrack(domains):
    if all(len(domains[i]) == 1 for i in range(81)):
        return [domains[i][0] for i in range(81)]
    n, idx = min((len(domains[i]), i) for i in range(81) if len(domains[i]) > 1)
    for val in domains[idx]:
        new_domains = [d[:] for d in domains]
        new_domains[idx] = [val]
        if ac3(new_domains):
            result = backtrack(new_domains)
            if result:
                return result
    return None

def solve_your_version(puzzle):
    domains = []
    for ch in puzzle:
        if ch in '123456789':
            domains.append([ch])
        else:
            domains.append(list('123456789'))
    if not ac3(domains):
        return None
    return backtrack(domains)

# ========== GOOGLE OR-TOOLS SOLVER ===========

def solve_with_ortools(puzzle):
    model = cp_model.CpModel()
    grid = [[model.NewIntVar(1,9,f'cell_{r}_{c}') for c in range(9)] for r in range(9)]
    
    for i in range(9):
        model.AddAllDifferent([grid[i][j] for j in range(9)])
        model.AddAllDifferent([grid[j][i] for j in range(9)])

    for i in range(3):
        for j in range(3):
            model.AddAllDifferent([grid[r][c] for r in range(i*3,i*3+3) for c in range(j*3,j*3+3)])

    for i in range(9):
        for j in range(9):
            val = puzzle[i*9+j]
            if val in '123456789':
                model.Add(grid[i][j] == int(val))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        return [solver.Value(grid[i][j]) for i in range(9) for j in range(9)]
    else:
        return None

# ========== GITHUB VERSION (Simple Backtracking) ===========

def str_to_board(puzzle):
    return [[int(puzzle[i*9+j]) if puzzle[i*9+j] != '0' else 0 for j in range(9)] for i in range(9)]

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    row, col = pos
    if num in board[row]: return False
    if num in [board[i][col] for i in range(9)]: return False
    startRow, startCol = (row//3)*3, (col//3)*3
    for i in range(startRow, startRow+3):
        for j in range(startCol, startCol+3):
            if board[i][j] == num:
                return False
    return True

def solve_git(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_valid(board, i, (row,col)):
            board[row][col] = i
            if solve_git(board):
                return True
            board[row][col] = 0
    return False

def solve_github(puzzle):
    board = str_to_board(puzzle)
    solve_git(board)
    return [board[i][j] for i in range(9) for j in range(9)]

# ========== SOLVING & TIMING ===========

def print_solution(solution):
    for r in range(9):
        print(' '.join(str(solution[r*9+c]) for c in range(9)))

#My method
your_start = time.time()
print("\n==== Solving with My Version ====")
your_solutions = []
for idx, p in enumerate(puzzles):
    print(f"\nPuzzle {idx+1}:")
    sol = solve_your_version(p)
    your_solutions.append(sol)
    print_solution(sol)
your_end = time.time()

# Google OR Tools
or_start = time.time()
print("\n==== Solving with GOOGLE OR-TOOLS ====")
or_solutions = []
for idx, p in enumerate(puzzles):
    print(f"\nPuzzle {idx+1}:")
    sol = solve_with_ortools(p)
    or_solutions.append(sol)
    print_solution(sol)
or_end = time.time()

# Github version
git_start = time.time()
print("\n==== Solving with GITHUB Version ====")
git_solutions = []
for idx, p in enumerate(puzzles):
    print(f"\nPuzzle {idx+1}:")
    sol = solve_github(p)
    git_solutions.append(sol)
    print_solution(sol)
git_end = time.time()

# ========== TIME COMPARISON ===========

print("\n======= TIME COMPARISON =======")
print(f"My Version Time: {round(your_end - your_start, 4)} seconds")
print(f"Google OR Tools Time: {round(or_end - or_start, 4)} seconds")
print(f"GitHub Version Time: {round(git_end - git_start, 4)} seconds")
