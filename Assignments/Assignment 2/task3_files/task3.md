### 1. My Implementation (AC-3 + Backtracking)
Models each puzzle as a CSP.

Uses AC-3 to eliminate inconsistent values.

Uses backtracking with the MRV heuristic.

Solves puzzles from a file and writes solutions back.

Includes timing using time.time().

![Screenshot 2025-04-26 221237](https://github.com/user-attachments/assets/0229eccb-c643-4401-8743-a5a8d619410a)


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


![Screenshot 2025-04-26 221311](https://github.com/user-attachments/assets/174e384a-66b6-4c48-97bc-5b61f824c98a)


### How Can I Improve My Version?

Add degree heuristic or least-constraining value ordering.
Add forward checking after assignment.
Use a deque for AC-3 queue for performance.

Overall, implemented a Sudoku solver using CSP techniques, and compared it with advanced solver tools like Google OR-Tools and simple online backtracking methods



