![image](https://github.com/user-attachments/assets/d30e86b0-9090-4020-9e71-296254c9ed4a)
![image](https://github.com/user-attachments/assets/ba3afdfb-a6c2-4b47-90f4-deca9acd1d04)

### Minimax Algorithm: The Strategy
Goal: Find the best move for Max by simulating all future moves.

How It Works:
DFS Exploration: Go deep into the tree (like a robot playing out all possible games).

Evaluate Leaves: At the end (leaf nodes), assign scores:

+1 if Max wins, -1 if Min wins, 0 for a draw.

Backpropagate: Bubble up scores:

At Max’s turn, pick the highest child value.

At Min’s turn, pick the lowest child value

![image](https://github.com/user-attachments/assets/d00854d6-e1d5-4157-ae0f-38dd82080adb)

###  Alpha-Beta Pruning: The Shortcut
Problem: Minimax is slow (checks every possible move).
Solution: Prune (ignore) branches that won’t change the outcome.

Key Terms:
Alpha (α): Best score Max can guarantee. Starts at -∞.

Beta (β): Best score Min can guarantee. Starts at +∞.

Prune when: α ≥ β (Max’s minimum is better than Min’s maximum → no need to keep checking)

![image](https://github.com/user-attachments/assets/ab28be52-f324-40d3-8822-c3c757a5fddc)


Minimax Python Code:
1. Node that potrays a game state:
   ![image](https://github.com/user-attachments/assets/95dc213b-9cfc-4670-96be-0a1d25d6fda6)

2. Minimax Agent
   ![image](https://github.com/user-attachments/assets/a3461cdd-d65a-46ae-aa71-b020d1722f66)

3. Environment that helps manage the game tree
   ![image](https://github.com/user-attachments/assets/7586395a-713a-43f1-bf16-0d1e5c2b8af1)

"Agent asks, Environment computes, Nodes remember."

Agent sets the depth.

Environment does DFS + backpropagation.

Nodes store minmax_value for reuse.

### Alpha-Beta Code
![image](https://github.com/user-attachments/assets/1191f26d-f432-48f7-9395-eb440d92af6e)


