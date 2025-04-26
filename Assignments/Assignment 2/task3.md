### 1. My Implementation (AC-3 + Backtracking)
Models each puzzle as a CSP.

Uses AC-3 to eliminate inconsistent values.

Uses backtracking with the MRV heuristic.

Solves puzzles from a file and writes solutions back.

Includes timing using time.time().

![Screenshot 2025-04-26 221707](https://github.com/user-attachments/assets/ae107590-a2df-4839-9669-58a4aa75081f)


### 2. Google OR-Tools Version
Uses Google's CP-SAT solver (constraint programming engine).

Much faster and more efficient.

Constraints are added via high-level modelling (AddAllDifferent).

Automatically uses propagation and search strategies internally.

![Screenshot 2025-04-26 221250](https://github.com/user-attachments/assets/4b0c8052-cf19-462a-a2b1-a51e1102ce24)


### 3. GitHub / ChatGPT Version
Pure backtracking.

No constraint propagation or heuristics.

Slower, especially for harder puzzles.

More readable but not efficient.

![Screenshot 2025-04-26 221302](https://github.com/user-attachments/assets/bcf5b7d3-f54d-4462-825f-1283fa4760cb)






## Differences Between Versions

| Feature                  | My Version        | OR-Tools          | GitHub Version |
|--------------------------|-------------------|--------------------|---------------------------|
| Constraint Propagation   | AC-3              | Built-in           | None                      |
| Heuristics (MRV, etc.)   | MRV               | Internal           | None                      |
| Speed                    | Medium            | Fast               | Slow                      |
| Customizability          | High              | Moderate           | High                      |
| Code Simplicity          | Medium            | Medium             | Very Simple               |


![Screenshot 2025-04-26 221941](https://github.com/user-attachments/assets/2b201a6f-a574-492e-8ad8-c6164db8e9eb)


### How Can I Improve My Version?


Add degree heuristic or least-constraining value ordering.
Add forward checking after assignment.
Use a deque for AC-3 queue for performance.

Overall, implemented a Sudoku solver using CSP techniques, and compared it with advanced solver tools like Google OR-Tools and simple online backtracking methods



