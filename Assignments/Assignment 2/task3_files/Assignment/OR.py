from ortools.sat.python import cp_model
import time

def solve_sudoku_with_ortools(puzzle):
    model = cp_model.CpModel()
    grid = [[model.NewIntVar(1, 9, f'cell_{r}_{c}') for c in range(9)] for r in range(9)]

    # Row, column, and block constraints
    for i in range(9):
        model.AddAllDifferent([grid[i][j] for j in range(9)])  # Rows
        model.AddAllDifferent([grid[j][i] for j in range(9)])  # Columns

    for i in range(3):
        for j in range(3):
            block = [grid[r][c] for r in range(i * 3, i * 3 + 3)
                                 for c in range(j * 3, j * 3 + 3)]
            model.AddAllDifferent(block)

    # Initial puzzle values
    for i in range(9):
        for j in range(9):
            val = puzzle[i * 9 + j]
            if val in '123456789':
                model.Add(grid[i][j] == int(val))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        return [solver.Value(grid[i][j]) for i in range(9) for j in range(9)]
    else:
        return None

def solve_all_with_ortools(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        puzzles = []
        for i in range(0, len(lines), 9):
            puzzle = ''.join(lines[i:i+9])
            if len(puzzle) == 81:
                puzzles.append(puzzle)

    print(f"\n📁 Found {len(puzzles)} puzzle(s)")
    print(f"🔧 Solving with Google OR-Tools...\n")
    start = time.time()

    for i, puzzle in enumerate(puzzles):
        print(f"\n🧩 Puzzle {i + 1}:")
        solution = solve_sudoku_with_ortools(puzzle)
        if solution:
            for r in range(9):
                print(' '.join(str(solution[r * 9 + c]) for c in range(9)))
        else:
            print("❌ No solution found.")

    end = time.time()
    print(f"\n⏱️ Time taken by OR-Tools: {round(end - start, 4)} seconds")

# 🔥 RUN THIS
if __name__ == "__main__":
    solve_all_with_ortools("sudoku_input.txt")
