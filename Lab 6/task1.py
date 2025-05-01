import math
from typing import List, Tuple, Optional

class CheckersGame:
    def __init__(self):
        # Initialize the 8x8 checkers board
        # 'B' = Black (AI), 'W' = White (Player), '.' = Empty
        # 'BK' = Black King, 'WK' = White King
        self.board = [
            ['.', 'B', '.', 'B', '.', 'B', '.', 'B'],
            ['B', '.', 'B', '.', 'B', '.', 'B', '.'],
            ['.', 'B', '.', 'B', '.', 'B', '.', 'B'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['W', '.', 'W', '.', 'W', '.', 'W', '.'],
            ['.', 'W', '.', 'W', '.', 'W', '.', 'W'],
            ['W', '.', 'W', '.', 'W', '.', 'W', '.']
        ]
        self.current_player = 'W'  # White (human) starts first

    def print_board(self):
        """Print the current board state with row/column labels"""
        print("  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.board):
            print(i, ' '.join(row))

    def is_valid_position(self, x: int, y: int) -> bool:
        """Check if coordinates are within the 8x8 board"""
        return 0 <= x < 8 and 0 <= y < 8

    def get_possible_moves(self, x: int, y: int) -> List[Tuple[int, int]]:
        """
        Get all valid moves for a piece at (x,y)
        Returns list of (new_x, new_y) positions
        """
        moves = []
        piece = self.board[x][y]

        if piece == '.':  # Empty spot
            return moves

        # Regular pieces can only move diagonally forward
        if piece == 'W':
            directions = [(-1, -1), (-1, 1)]  # White moves up
        elif piece == 'B':
            directions = [(1, -1), (1, 1)]    # Black moves down
        else:  # Kings can move in all diagonal directions
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.is_valid_position(new_x, new_y):
                if self.board[new_x][new_y] == '.':  # Regular move
                    moves.append((new_x, new_y))
                else:  # Possible capture
                    jump_x, jump_y = new_x + dx, new_y + dy
                    if (self.is_valid_position(jump_x, jump_y) and 
                        self.board[jump_x][jump_y] == '.' and
                        self.board[new_x][new_y].upper() != piece.upper()):
                        moves.append((jump_x, jump_y))
        return moves

    def make_move(self, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        """
        Execute a move and handle captures
        Returns True if move was valid, False otherwise
        """
        start_x, start_y = start
        end_x, end_y = end

        # Check if move is valid
        if (not self.is_valid_position(*start) or 
            not self.is_valid_position(*end) or
            self.board[start_x][start_y] != self.current_player):
            return False

        possible_moves = self.get_possible_moves(start_x, start_y)
        if end not in possible_moves:
            return False

        # Execute the move
        piece = self.board[start_x][start_y]
        self.board[start_x][start_y] = '.'
        self.board[end_x][end_y] = piece

        # Handle capture (if it's a jump move)
        if abs(start_x - end_x) == 2:
            captured_x = (start_x + end_x) // 2
            captured_y = (start_y + end_y) // 2
            self.board[captured_x][captured_y] = '.'

        # Check for promotion to king
        if (piece == 'W' and end_x == 0) or (piece == 'B' and end_x == 7):
            self.board[end_x][end_y] = piece.upper()  # W → WK, B → BK

        # Switch players
        self.current_player = 'B' if self.current_player == 'W' else 'W'
        return True

    def evaluate_board(self) -> int:
        """
        Heuristic evaluation of board state
        Positive = good for AI (Black), Negative = good for Player (White)
        """
        score = 0
        for row in self.board:
            for piece in row:
                if piece == 'B':
                    score += 1
                elif piece == 'BK':
                    score += 3  # Kings are more valuable
                elif piece == 'W':
                    score -= 1
                elif piece == 'WK':
                    score -= 3
        return score

    def minimax(self, depth: int, alpha: float, beta: float, is_maximizing: bool) -> int:
        """
        Minimax algorithm with Alpha-Beta pruning
        Returns the best evaluation score for the current board state
        """
        if depth == 0 or self.is_game_over():
            return self.evaluate_board()

        if is_maximizing:  # AI's turn (Black)
            max_eval = -math.inf
            for move in self.get_all_possible_moves('B'):
                # Make a copy to simulate moves without affecting real board
                board_copy = [row[:] for row in self.board]
                self.make_move(move[0], move[1])
                evaluation = self.minimax(depth-1, alpha, beta, False)
                self.board = [row[:] for row in board_copy]  # Undo move
                
                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval
        else:  # Player's turn (White)
            min_eval = math.inf
            for move in self.get_all_possible_moves('W'):
                board_copy = [row[:] for row in self.board]
                self.make_move(move[0], move[1])
                evaluation = self.minimax(depth-1, alpha, beta, True)
                self.board = [row[:] for row in board_copy]
                
                min_eval = min(min_eval, evaluation)
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval

    def get_all_possible_moves(self, player: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
        """
        Get all possible moves for a player
        Returns list of ((start_x, start_y), (end_x, end_y)) moves
        """
        moves = []
        for x in range(8):
            for y in range(8):
                if self.board[x][y].upper() == player.upper():
                    for end_pos in self.get_possible_moves(x, y):
                        moves.append(((x, y), end_pos))
        return moves

    def is_game_over(self) -> bool:
        """Check if game has ended (no pieces left or no valid moves)"""
        # Count pieces
        white_pieces = sum(row.count('W') + row.count('WK') for row in self.board)
        black_pieces = sum(row.count('B') + row.count('BK') for row in self.board)
        if white_pieces == 0 or black_pieces == 0:
            return True
        
        # Check if current player has any valid moves
        current_pieces = 'W' if self.current_player == 'W' else 'B'
        return len(self.get_all_possible_moves(current_pieces)) == 0

    def ai_move(self, depth: int = 3) -> Optional[Tuple[Tuple[int, int], Tuple[int, int]]]:
        """
        AI makes a move using Minimax with Alpha-Beta pruning
        Returns the best move found ((start_x, start_y), (end_x, end_y))
        """
        best_move = None
        best_eval = -math.inf
        alpha = -math.inf
        beta = math.inf

        for move in self.get_all_possible_moves('B'):
            # Simulate move
            board_copy = [row[:] for row in self.board]
            self.make_move(move[0], move[1])
            
            # Evaluate move
            evaluation = self.minimax(depth-1, alpha, beta, False)
            
            # Undo move
            self.board = [row[:] for row in board_copy]
            
            # Update best move
            if evaluation > best_eval:
                best_eval = evaluation
                best_move = move

        return best_move

# Main game loop
def play_checkers():
    game = CheckersGame()
    print("Welcome to Checkers!")
    print("You're White (W), AI is Black (B)")
    print("Enter moves as 'start_row start_col end_row end_col' (e.g., '2 3 3 4')")

    while not game.is_game_over():
        game.print_board()
        
        if game.current_player == 'W':  # Human turn
            while True:
                try:
                    move = input("Your move: ").split()
                    if len(move) != 4:
                        print("Please enter 4 numbers separated by spaces")
                        continue
                    start = (int(move[0]), int(move[1]))
                    end = (int(move[2]), int(move[3]))
                    
                    if game.make_move(start, end):
                        break
                    else:
                        print("Invalid move! Try again.")
                except ValueError:
                    print("Please enter numbers only!")
        else:  # AI turn
            print("AI is thinking...")
            ai_move = game.ai_move()
            if ai_move:
                start, end = ai_move
                print(f"AI moves: {start} → {end}")
                game.make_move(start, end)
            else:
                print("AI has no valid moves!")
                break

    # Game over
    game.print_board()
    white_pieces = sum(row.count('W') + row.count('WK') for row in game.board)
    black_pieces = sum(row.count('B') + row.count('BK') for row in game.board)
    
    if white_pieces == 0 or black_pieces > white_pieces:
        print("AI (Black) wins!")
    elif black_pieces == 0 or white_pieces > black_pieces:
        print("You (White) win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_checkers()
