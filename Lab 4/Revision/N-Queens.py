#Two types of Supervised Learning 
#Classification Pick a category 
#Regression Predict a number

 

#N-Queens cause no two queens are the same!
from ortools.sat.python import cp_model
def solve_n_queens(n):
    model = cp_model.CpModel()
    
    #Create Variables: queen[i] is the colunm of the queen in row i
    queens = [model.new_int_var(0, n-1, f'Q{i}') for i in range(n)]
    
    #Constraint all queens must be in a different colunm
    model.add_all_different(queens)
    
    #Constraint 2 : Queens cannot be diagonal 
    for i in range(n):
        for j in range(i+1, n):
            #Diagonal: abs(col[i] - col[j] != abs(i-j)
            model.add(queens[i] != queens[j])
            model.add(queens[i] -i != queens[j] -j)
            model.add(queens[i]+ i != queens[j]+ j)
            
    #solve
    solver = cp_model.CpSolver()
    status = solver.solve(model)
    
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        for i in range(n):
            row = ['.']*n
            row[solver.value(queens[i])] = 'Q'
            print(" ".join(row))
            
    else:
        print("No solution found")

solve_n_queens(10)
 
