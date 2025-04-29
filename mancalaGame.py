import random

# Core game logic for Mancala
class MancalaGame:
    def __init__(self, board=None, playerTurn=0):
        # Initialize a board with 4 stones per pit and empty Mancalas
        self.board = board or [4] * 6 + [0] + [4] * 6 + [0]
        self.turn = playerTurn  # 0 for Player 0, 1 for Player 1

    # Return a copy of the game state
    def clone(self):
        return MancalaGame(self.board.copy(), self.turn)

    # Return list of valid pits that the current player can choose
    def validMoves(self):
        start = 0 if self.turn == 0 else 7
        return [i for i in range(start, start + 6) if self.board[i] > 0]

    # Check if game has ended (one side is empty)
    def gameOver(self):
        return all(stone == 0 for stone in self.board[0:6]) or all(stone == 0 for stone in self.board[7:13])

    # Apply a move: sow stones, handle capturing, and switch turns
    def applyMove(self, pit):
        stones = self.board[pit]
        self.board[pit] = 0
        index = pit
        while stones > 0:
            index = (index + 1) % 14
            # Skip opponent's Mancala
            if (self.turn == 0 and index == 13) or (self.turn == 1 and index == 6):
                continue
            self.board[index] += 1
            stones -= 1
        
        # Handle capturing rule
        if self.turn == 0 and 0 <= index <= 5 and self.board[index] == 1:
            opposite = 12 - index
            self.board[6] += self.board[opposite] + 1
            self.board[index] = 0
            self.board[opposite] = 0
        elif self.turn == 1 and 7 <= index <= 12 and self.board[index] == 1:
            opposite = 12 - index
            self.board[13] += self.board[opposite] + 1
            self.board[index] = 0
            self.board[opposite] = 0

        # Switch turn
        self.turn = 1 - self.turn

    # Sweep remaining stones into Mancalas when game ends
    def finishGame(self):
        if all(stone == 0 for stone in self.board[0:6]):
            self.board[13] += sum(self.board[7:13])
            for i in range(7, 13):
                self.board[i] = 0
        elif all(stone == 0 for stone in self.board[7:13]):
            self.board[6] += sum(self.board[0:6])
            for i in range(0, 6):
                self.board[i] = 0

    # Return winner: 0 for Player 0, 1 for Player 1, -1 for tie
    def winner(self):
        self.finishGame()
        if self.board[6] > self.board[13]:
            return 0
        elif self.board[13] > self.board[6]:
            return 1
        else:
            return -1


# --- AI Player Classes ---

# Player that picks a random valid move
class RandomPlayer:
    def chooseMove(self, game: MancalaGame):
        return random.choice(game.validMoves())

# Player using minimax search up to given depth
class MinimaxPlayer:
    def __init__(self, depth=5):
        self.depth = depth

    def chooseMove(self, game: MancalaGame):
        _, move = self.minimax(game, self.depth, True)
        return move

    # Basic Minimax algorithm without pruning
    def minimax(self, game, depth, maximizing):
        if depth == 0 or game.gameOver():
            return self.evaluate(game), None

        moves = game.validMoves()
        bestMove = None

        if maximizing:
            maxEval = float('-inf')
            for move in moves:
                clone = game.clone()
                clone.applyMove(move)
                eval, _ = self.minimax(clone, depth - 1, False)
                if eval > maxEval:
                    maxEval = eval
                    bestMove = move
            return maxEval, bestMove
        else:
            minEval = float('inf')
            for move in moves:
                clone = game.clone()
                clone.applyMove(move)
                eval, _ = self.minimax(clone, depth - 1, True)
                if eval < minEval:
                    minEval = eval
                    bestMove = move
            return minEval, bestMove

    # Evaluation: difference in Mancala scores
    def evaluate(self, game):
        return game.board[6] - game.board[13]

# Player using Alpha-Beta pruning
class AlphaBetaPlayer(MinimaxPlayer):
    def chooseMove(self, game: MancalaGame):
        _, move = self.alphabeta(game, self.depth, float('-inf'), float('inf'), True)
        return move

    def alphabeta(self, game, depth, alpha, beta, maximizing):
        if depth == 0 or game.gameOver():
            return self.evaluate(game), None

        moves = game.validMoves()
        bestMove = None

        if maximizing:
            maxEval = float('-inf')
            for move in moves:
                clone = game.clone()
                clone.applyMove(move)
                eval, _ = self.alphabeta(clone, depth - 1, alpha, beta, False)
                if eval > maxEval:
                    maxEval = eval
                    bestMove = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
            return maxEval, bestMove
        else:
            minEval = float('inf')
            for move in moves:
                clone = game.clone()
                clone.applyMove(move)
                eval, _ = self.alphabeta(clone, depth - 1, alpha, beta, True)
                if eval < minEval:
                    minEval = eval
                    bestMove = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return minEval, bestMove

# Player with advanced evaluation heuristics
class AdvancedAlphaBetaPlayer(AlphaBetaPlayer):
    def evaluate(self, game):
        board = game.board
        player = game.turn
        opponent = 1 - player
        myMancala = board[6 if player == 0 else 13]
        oppMancala = board[13 if player == 0 else 6]

        myPits = board[0:6] if player == 0 else board[7:13]
        oppPits = board[7:13] if player == 0 else board[0:6]

        pitDiff = sum(myPits) - sum(oppPits)
        
        # Encourage winning earlier
        endgameBonus = 0
        if game.gameOver():
            endgameBonus = 20 if myMancala > oppMancala else -20

        return (myMancala - oppMancala) + 0.4 * pitDiff + endgameBonus