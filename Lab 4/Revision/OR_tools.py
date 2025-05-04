#Map colring problem

from ortools.sat.python import cp_model

#2 Create a model 
model = cp_model.CpModel()

#3 Create variables with domain 0 - 2 each representing in this case a color
x= model.new_int_var(0,2,"x")
y= model.new_int_var(0,2,"y")
z= model.new_int_var(0,2,"z")

#4 Add constraints 
model.add(x != y)
model.add(y != z)
model.add(x != z)

#5 Solve 
solver = cp_model.CpSolver()
status = solver.solve(model)

#6 Print Result
if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
  print("x (A) =", solver.value(x))
  print("y (B) =", solver.value(y))
  print("z (C) =" solver.value(z))

else:
  print("No solution found")
                        
