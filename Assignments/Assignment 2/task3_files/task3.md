### 
1. My Implementation (AC-3 + Backtracking)
Models each puzzle as a CSP.

Uses AC-3 to eliminate inconsistent values.

Uses backtracking with the MRV heuristic.

Solves puzzles from a file and writes solutions back.

Includes timing using time.time().

![Screenshot 2025-04-16 183134](https://github.com/user-attachments/assets/8ed398d6-2bfc-47fa-8986-f31fd3d6db84)


###
 2. Google OR-Tools Version
Uses Google's CP-SAT solver (constraint programming engine).

Much faster and more efficient.

Constraints are added via high-level modelling (AddAllDifferent).

Automatically uses propagation and search strategies internally.

![Screenshot 2025-04-16 183100](https://github.com/user-attachments/assets/c507bde3-30ee-41b4-b677-f580b3067df4)

###
3. GitHub / ChatGPT Version
Pure backtracking.

No constraint propagation or heuristics.

Slower, especially for harder puzzles.

More readable but not efficient.

![Screenshot 2025-04-16 183716](https://github.com/user-attachments/assets/f23c2f32-d3a2-4dcb-abea-ce08c907c266)







## Differences Between Versions

| Feature                  | My Version        | OR-Tools          | GitHub Version |
|--------------------------|-------------------|--------------------|---------------------------|
| Constraint Propagation   | AC-3              | Built-in           | None                      |
| Heuristics (MRV, etc.)   | MRV               | Internal           | None                      |
| Speed                    | Medium            | Fast               | Slow                      |
| Customizability          | High              | Moderate           | High                      |
| Code Simplicity          | Medium            | Medium             | Very Simple               |
