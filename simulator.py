import time
import mancalaGame  # Import the core game logic and AI players

# Run n simulated games between player1 and player2
def simulateGames(player1, player2, n=100, showTime=False):
    wins = [0, 0]
    ties = 0
    totalTurns = 0
    totalTime = 0
    MAXTURNS = 200

    for _ in range(n):
        game = mancalaGame.MancalaGame()
        turns = 0
        start = time.time()

        # Play until game ends or max turns reached
        while not game.gameOver() and turns < MAXTURNS:
            player = player1 if game.turn == 0 else player2
            move = player.chooseMove(game)
            game.applyMove(move)
            turns += 1

        duration = time.time() - start
        totalTime += duration
        totalTurns += turns

        winner = game.winner()
        if winner == -1:
            ties += 1
        else:
            wins[winner] += 1

    # Compute and return statistics
    result = {
        "Player 1 Win %": wins[0] / n * 100,
        "Player 2 Win %": wins[1] / n * 100,
        "Tie %": ties / n * 100,
        "Average Moves": totalTurns / n,
    }
    if showTime:
        result["Average Time per Game (s)"] = totalTime / n
    return result

# Run simulations between various AI pairs
def runSim():
    print("Running 100 games: Random Player vs. Random Player")
    rVr = simulateGames(mancalaGame.RandomPlayer(), mancalaGame.RandomPlayer())
    for k, v in rVr.items():
        print(f"{k}: {v:.2f}")

    print("\nRunning 100 games: Minimax AI vs. Random Player (depth=5)")
    minimaxVr = simulateGames(mancalaGame.MinimaxPlayer(depth=5), mancalaGame.RandomPlayer())
    for k, v in minimaxVr.items():
        print(f"{k}: {v:.2f}")

    print("\nRunning 100 games: Alpha-Beta AI vs. Random Player (depth=5)")
    alphabetaVr = simulateGames(mancalaGame.AlphaBetaPlayer(depth=5), mancalaGame.RandomPlayer(), showTime=True)
    for k, v in alphabetaVr.items():
        print(f"{k}: {v:.2f}")

# Run simulation with the most advanced AI
def runAdvancedSim():
    print("\nRunning 100 games: Advanced Alpha-Beta (depth=10) vs Random Player")
    advancedVr = simulateGames(mancalaGame.AdvancedAlphaBetaPlayer(depth=10), mancalaGame.RandomPlayer(), showTime=True)
    for k, v in advancedVr.items():
        print(f"{k}: {v:.2f}")

# Interactive loop for simulation
if __name__ == '__main__':
    while True:
        choice = input("Would you like to run a simulation? (y/n): ").strip().lower()
        if choice == 'y':
            runSim()
            runAdvancedSim()
        elif choice == 'n':
            break
        else:
            print('Invalid input')