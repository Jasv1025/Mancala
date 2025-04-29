import mancalaGame  # Import the core game logic and AI players

# Display the current state of the board in a formatted way
def board(board):
    print("\n   12  11  10   9   8   7")
    print(" +---+---+---+---+---+---+")
    print(f" | {' | '.join(f'{board[i]:2}' for i in range(12, 6, -1))} |")
    print(f"{board[13]:2}                       {board[6]:2}")
    print(f" | {' | '.join(f'{board[i]:2}' for i in range(0, 6))} |")
    print(" +---+---+---+---+---+---+")
    print("    0   1   2   3   4   5\n")

# Get a valid move from a human player
def humanMove(game):
    move = None
    while move not in game.validMoves():
        try:
            move = int(input(f"Player {game.turn}, choose a pit "
                             f"({'0-5' if game.turn == 0 else '7-12'}): "))
            if move not in game.validMoves():
                print("Invalid move. Pick one of your own pits that has stones.")
        except ValueError:
            print("Please enter a valid integer.")
    return move

# Main game loop between two players (either humans or AI)
def play(player0, player1):
    game = mancalaGame.MancalaGame()

    # Loop until game over
    while not game.gameOver():
        board(game.board)
        current_player = player0 if game.turn == 0 else player1

        # Human vs AI check
        if isinstance(current_player, str) and current_player == "human":
            move = humanMove(game)
        else:
            move = current_player.chooseMove(game)
            print(f"AI Player {game.turn} chose move: {move}")

        game.applyMove(move)

    # Finish game and display result
    game.finishGame()
    board(game.board)
    winner = game.winner()
    if winner == -1:
        print("🏁 The game is a tie!")
    else:
        print(f"Player {winner} wins!")

# CLI menu for selecting game mode
def menu():
    print("\n=== Mancala Game ===")
    print("1. Human vs Human")
    print("2. Human vs Random AI")
    print("3. Human vs Minimax AI (depth=5)")
    print("4. Human vs Alpha-Beta AI (depth=5)")
    print("5. Human vs Advanced Alpha-Beta AI (depth=10)")
    choice = input("Choose a mode (1-5): ")

    # Match choice to appropriate players and start game
    if choice == "1":
        play("human", "human")
    elif choice == "2":
        turn = int(input("Play as Player 0 or 1? (enter 0 or 1): "))
        if turn == 0:
            play("human", mancalaGame.RandomPlayer())
        else:
            play(mancalaGame.RandomPlayer(), "human")
    elif choice == "3":
        turn = int(input("Play as Player 0 or 1? (enter 0 or 1): "))
        if turn == 0:
            play("human", mancalaGame.MinimaxPlayer(depth=5))
        else:
            play(mancalaGame.MinimaxPlayer(depth=5), "human")
    elif choice == "4":
        turn = int(input("Play as Player 0 or 1? (enter 0 or 1): "))
        if turn == 0:
            play("human", mancalaGame.AlphaBetaPlayer(depth=5))
        else:
            play(mancalaGame.AlphaBetaPlayer(depth=5), "human")
    elif choice == "5":
        turn = int(input("Play as Player 0 or 1? (enter 0 or 1): "))
        if turn == 0:
            play("human", mancalaGame.AdvancedAlphaBetaPlayer(depth=10))
        else:
            play(mancalaGame.AdvancedAlphaBetaPlayer(depth=10), "human")
    else:
        print("Invalid option. Please run again.")

# Launch menu if script is run directly
if __name__ == '__main__':
    menu()