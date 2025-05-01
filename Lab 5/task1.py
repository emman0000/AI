
import chess
import chess.engine

def beam_search_chess(board, beam_width=3, depth_limit=2, evaluation_time=0.1):
    """
    Perform beam search to find the best move sequence in chess.
    
    Args:
        board: chess.Board - current board state
        beam_width: int - number of top moves to keep at each level
        depth_limit: int - how many plies (half-moves) to look ahead
        evaluation_time: float - time to spend evaluating each position
        
    Returns:
        tuple: (best_move_sequence, best_score)
    """
    # Initialize the chess engine (Stockfish)
    try:
        engine = chess.engine.SimpleEngine.popen_uci("stockfish")
    except:
        raise Exception("Stockfish engine not found. Please install Stockfish and add it to PATH.")
    
    # Store sequences and their scores
    current_beam = [([], board, 0)]  # (move_sequence, board, score)
    
    for depth in range(depth_limit):
        next_beam = []
        
        for move_sequence, current_board, current_score in current_beam:
            # Generate all legal moves
            for move in current_board.legal_moves:
                # Make a copy of the board to simulate the move
                new_board = current_board.copy()
                new_board.push(move)
                
                # Evaluate the new position
                info = engine.analyse(new_board, chess.engine.Limit(time=evaluation_time))
                score = info["score"].relative.score()
                
                # If score is None (checkmate), assign extreme value
                if score is None:
                    score = float('inf') if new_board.turn == chess.WHITE else float('-inf')
                
                # Add to next beam candidates
                new_sequence = move_sequence + [move]
                next_beam.append((new_sequence, new_board, score))
        
        # Sort all candidates by score (higher is better for white)
        next_beam.sort(key=lambda x: x[2], reverse=board.turn == chess.WHITE)
        
        # Keep only the top beam_width candidates
        current_beam = next_beam[:beam_width]
        
        # If no moves left, break early
        if not current_beam:
            break
    
    # Close the engine
    engine.quit()
    
    # Return the best sequence found
    if current_beam:
        best_sequence, best_board, best_score = current_beam[0]
        return best_sequence, best_score
    else:
        return [], 0

# Example usage
if __name__ == "__main__":
    board = chess.Board()
    beam_width = 3
    depth_limit = 2
    
    best_sequence, best_score = beam_search_chess(board, beam_width, depth_limit)
    
    print("Best move sequence:")
    for move in best_sequence:
        print(move.uci(), end=" ")
    print(f"\nEvaluation score: {best_score}")
