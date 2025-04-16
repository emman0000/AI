import time

def read_puzzles(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if len(line.strip()) == 81]

def write_solutions(filename, solutions):
    with open(filename, 'w') as f:
        for solution in solutions:
            f.write(''.join(str(c) for c in solution) + '\n')

def display(grid):
    for r in range(9):
        print(' '.join(str(c) for c in grid[r*9:(r+1)*9]))

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

def solve(puzzle):
    domains = []
    for ch in puzzle:
        if ch in '123456789':
            domains.append([ch])
        else:
            domains.append(list('123456789'))
    if not ac3(domains):
        return None
    return backtrack(domains)

def solve_all():
    puzzles = read_puzzles(r"C:\Users\thisp\Desktop\Assignment\sudoku_input.txt")
    solutions = []
    print(f"Loaded {len(puzzles)} puzzles")
    start_time = time.time()

    for i, puzzle in enumerate(puzzles):
        print(f"\n Puzzle {i+1}:")
        display(list(puzzle))
        solution = solve(puzzle)

        if solution:
            print("\n Solved:")
            display(solution)
            solutions.append(solution)
        else:
            print("No solution found.")
            solutions.append(['.'] * 81)

    end_time = time.time()
    print(f"\nTotal Time: {round(end_time - start_time, 4)} seconds")
    write_solutions("sudoku_solutions.txt", solutions)

if __name__ == "__main__":
    solve_all()
