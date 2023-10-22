"""
The Agent class. Note that the agent has just a single minimax function.
The minimax function is used in a generic Game class
"""
import math

class Agent:
    def __init__(self, game, selfPiece, opponentPiece):
        self.game = game
        self.MIN = -float('inf')
        self.MAX = float('inf')
        self.winscore =  10000000
        self.losescore = -10000000
        self.selfPiece = selfPiece          #AI
        self.opponentPiece = opponentPiece  #HUMAN


    '''
    This is the function you must complete
    Inputs -
    1. self (Agent object reference)
    2. board (2d array)
    3. depth (float)
    4. maximizingPlayer (bool)
    5. alpha (float)
    6. beta (float)

    Outputs -
    1. score (float)
    2. next_move (type discussed below)

    Notes
    1. Need to create general implementation that considers all move types - tuple or float
    2. We use depth here to measure how far down we need to keep going, we stop at depth = 0
    3. Need to consider the different situations when game is over
    4. Prioritize winning in fewest moves
    5. next_move is the best possible move from valid_moves based on alpha-beta pruning. 
       Do not need to focus on its type, since it differs based on game, just find best move from valid_moves
    '''
    def minimax(self, board, depth, maximizingPlayer, alpha, beta):
        is_self_winner = self.game.is_winner(board, self.selfPiece)
        is_opponent_winner = self.game.is_winner(board, self.opponentPiece)
    
        if depth == 0 and not is_self_winner and not is_opponent_winner:
            return None, self.game.heuristic_value(board, self.selfPiece if maximizingPlayer else self.opponentPiece)
        else:
            if is_self_winner:
                return None, self.winscore
            elif is_opponent_winner:
                return None, self.losescore
        best_move = None
        valid_moves = self.game.get_valid_moves(board)
        best_val = self.MIN if maximizingPlayer else self.MAX
        for next_move in valid_moves:
            next_board = self.game.play_move(board, next_move, self.selfPiece if maximizingPlayer else self.opponentPiece)
            if self.game.is_winner(next_board, self.selfPiece if maximizingPlayer else self.opponentPiece):
                quick_value = self.winscore if maximizingPlayer else self.losescore
                if maximizingPlayer and quick_value > best_val:
                    best_val = quick_value
                    alpha = max(alpha, best_val)
                elif not maximizingPlayer and quick_value < best_val:
                    best_val = quick_value
                    beta = min(beta, best_val)
                if beta <= alpha:
                    break
                param = math.log(depth) * 0.25
                return next_move, best_val + (param if maximizingPlayer else -param)
            
            _, value = self.minimax(next_board, depth-1, not maximizingPlayer, alpha, beta)       
            if maximizingPlayer and value > best_val:
                best_move, best_val = next_move, value
                alpha = max(alpha, best_val)
            elif not maximizingPlayer and value < best_val:
                best_move, best_val = next_move, value
                beta = min(beta, best_val)
            if beta <= alpha:
                break
    
        param = math.log(depth) * 0.25
        return best_move, best_val + (param if maximizingPlayer else -param)




















 
        # is_board_full = self.game.is_full(board)
        # if depth == 0:
        #     is_self_winner = self.game.is_winner(board, self.selfPiece)
        #     is_opponent_winner = self.game.is_winner(board, self.opponentPiece)
        #     if not is_self_winner and not is_opponent_winner:
        #         return None, self.game.heuristic_value(board, self.selfPiece if maximizingPlayer else self.opponentPiece)
        #     else:
        #         if is_self_winner:
        #             return None, self.winscore
        #         elif is_opponent_winner:
        #             return None, self.losescore
        # if is_board_full:
        #     is_self_winner = self.game.is_winner(board, self.selfPiece)
        #     is_opponent_winner = self.game.is_winner(board, self.opponentPiece)
        #     if is_self_winner:
        #             return None, self.winscore
        #     elif is_opponent_winner:
        #             return None, self.losescore
        # is_self_winner = self.game.is_winner(board, self.selfPiece if maximizingPlayer else self.opponentPiece)
        # is_board_full = self.game.is_full(board)
        # if is_self_winner and maximizingPlayer:
        #     return None, self.winscore
        # elif is_self_winner and not maximizingPlayer:
        #     return None, self.losescore
        # elif depth == 0 or is_board_full:
        #     return None, self.game.heuristic_value(board, self.selfPiece if maximizingPlayer else self.opponentPiece)
            # else: 
            #     return None, self.losescore
        # Check for terminal states
#         is_self_winner = self.game.is_winner(board, self.selfPiece)
#         is_opponent_winner = self.game.is_winner(board, self.opponentPiece)
#         is_board_full = self.game.is_full(board)

# # Determine the return value based on terminal state and whose turn it is
#         if is_self_winner:
#             return None, self.winscore if maximizingPlayer else self.losescore
#         elif is_opponent_winner:
#             return None, self.losescore if maximizingPlayer else self.winscore
#         elif depth == 0 or is_board_full:
#             return None, self.game.heuristic_value(board, self.selfPiece if maximizingPlayer else self.opponentPiece)




        
#         best_move = None
#         valid_moves = self.game.get_valid_moves(board)
#         # valid_moves = sorted(valid_moves, key=lambda x: self.game.heuristic_value(self.game.play_move(board, x, self.selfPiece if maximizingPlayer else self.opponentPiece), self.selfPiece if maximizingPlayer else self.opponentPiece), reverse=maximizingPlayer)
#         best_val = self.MIN if maximizingPlayer else self.MAX
#         for next_move in valid_moves:
#             next_board = self.game.play_move(board, next_move, self.selfPiece if maximizingPlayer else self.opponentPiece)
#             # if self.game.is_winner(next_board, self.selfPiece if maximizingPlayer else self.opponentPiece):
#             #     return next_move, self.winscore if maximizingPlayer else self.losescore
#         # Run minimax for this move
#             _, value = self.minimax(next_board, depth-1, not maximizingPlayer, alpha, beta)
#             # Update best_val and best_move
#             if maximizingPlayer and value > best_val:
#                 best_move, best_val = next_move, value
#                 alpha = max(alpha, best_val)
#             elif not maximizingPlayer and value < best_val:
#                 best_move, best_val = next_move, value
#                 beta = min(beta, best_val)

#         # Alpha-beta pruning
#             if beta <= alpha:
#                 break

#         param = depth
#         return best_move, best_val + (param if maximizingPlayer else -param)


        # for next_move in valid_moves:
        #     next_board = self.game.play_move(board, next_move, self.selfPiece if maximizingPlayer else self.opponentPiece)
        #     if self.game.is_winner(next_board, self.selfPiece if maximizingPlayer else self.opponentPiece):
        #         return next_move, self.winscore

        # # for next_move in valid_moves:
           
        #     _, value = self.minimax(next_board, depth-1, not maximizingPlayer, alpha, beta)
        
        #     if maximizingPlayer and value > best_val:
        #         best_move, best_val = next_move, value
        #         alpha = max(alpha, best_val)
        #     elif not maximizingPlayer and value < best_val:
        #         best_move, best_val = next_move, value
        #         beta = min(beta, best_val)
        
        #     if beta <= alpha:
        #         break
        # param = depth
        # return best_move, best_val + (param if maximizingPlayer else -param)
    
        # if maximizingPlayer:
        #     best_val = self.MIN
        #     for next_move in valid_moves:
        #         next_board = self.game.play_move(board, next_move, self.selfPiece)
        #         _, value = self.minimax(next_board, depth-1, False, alpha, beta)
        #         if value > best_val:
        #             best_move, best_val = next_move, value
        #         alpha = max(alpha, best_val)
        #         if beta <= alpha:
        #             break
        #     # print(best_val) + 10 ** depth
        #     return best_move, best_val + depth
        # #math.log(depth)*0.25
        # #
        # else:
        #     best_val = self.MAX
        #     for next_move in valid_moves:
        #         next_board = self.game.play_move(board, next_move, self.opponentPiece)
        #         _, value = self.minimax(next_board, depth-1, True, alpha, beta)
        #         if value < best_val:
        #             best_move, best_val = next_move, value
        #         beta = min(beta, best_val)
        #         if beta <= alpha:
        #             break
        #     # print(best_val)
        #     return best_move, best_val - depth

        #depth * 0.25
    #     best_move = None
    #     best_value = self.MIN
    #     # for d in range(1, depth + 1):
    #     #     move, value = self.true_minimax(board, d, maximizingPlayer, alpha, beta)
    #     #     if maximizingPlayer and value > best_value:
    #     #         best_move, best_value = move, value
    #     #         alpha = max(alpha, value)
    #     #     elif not maximizingPlayer and value < best_value:
    #     #         best_move, best_value = move, value
    #     #         beta = min(beta, value)

    #     # return best_move, best_value
    #     for depth in range(1, depth + 1):
    #         move, value = self.true_minimax(board, depth, maximizingPlayer, alpha, beta)
    #         if value > best_value:
    #             best_move, best_value = move, value
    #     return best_move, best_value
            
    # def true_minimax(self, board, depth, maximizingPlayer, alpha, beta):
    #     if depth==0:
    #         if maximizingPlayer:
    #             return None, self.game.heuristic_value(board, 2)
    #         else:
    #             return None, self.game.heuristic_value(board, 1)
    #     best_move = None
    #     valid_moves = self.game.get_valid_moves(board)
    #     if maximizingPlayer:
    #         bestVal = self.MIN
    #         for next_move in valid_moves:
    #             next_board = self.game.play_move(board, next_move, 2)
    #             _, value = self.true_minimax(next_board, depth-1, False, alpha, beta)
    #             if value > bestVal:
    #                 best_move, bestVal = next_move, value
    #             alpha = max(alpha, bestVal)
    #             if beta <= alpha:
    #                 break
    #         return best_move, bestVal
    #     else:
    #         bestVal = self.MAX
    #         for next_move in valid_moves:
    #             next_board = self.game.play_move(board, next_move, 1)
    #             _, value = self.true_minimax(next_board, depth-1, True, alpha, beta)
    #             if value < bestVal:
    #                 best_move, bestVal = next_move, value 
    #             beta = min(beta, bestVal)
    #             if beta <= alpha:
    #                 break
    #         return  best_move, bestVal