from ortools.sat.python import cp_model

def solve_timetable():
    model = cp_model.CpModel()

    # Sample data
    teachers = ["T1", "T2"]
    classes = ["C1", "C2", "C3"]
    timeslots = list(range(5))  # 5 time slots
    rooms = list(range(2))      # 2 rooms

    # Variable: class_schedules[i] = (timeslot, room)
    time_vars = [model.new_int_var(0, len(timeslots) - 1, f"time_{c}") for c in classes]
    room_vars = [model.new_int_var(0, len(rooms) - 1, f"room_{c}") for c in classes]

    # Sample teacher mapping
    class_teachers = {"C1": "T1", "C2": "T1", "C3": "T2"}

   # Constraint 1: No two classes in the same room at the same time
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            ti, ri = time_vars[i], room_vars[i]
            tj, rj = time_vars[j], room_vars[j]

            # Create a boolean variable to represent "same room"
            same_room = model.new_bool_var(f"same_room_{i}_{j}")

            # same_room is true if ri == rj
            model.add(ri == rj).only_enforce_if(same_room)
            model.add(ri != rj).only_enforce_if(same_room.Not())

            # If same_room is true, then times must be different
            model.add(ti != tj).only_enforce_if(same_room)


    # Constraint 2: Same teacher can't teach two classes at same time
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            if class_teachers[classes[i]] == class_teachers[classes[j]]:
                model.add(time_vars[i] != time_vars[j])

    # Solve
    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        for i, c in enumerate(classes):
            print(f"{c}: Time = {solver.value(time_vars[i])}, Room = {solver.value(room_vars[i])}")
    else:
        print("No valid schedule found.")

solve_timetable()
