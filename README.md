<<<<<<< HEAD
# Mancala
Final project for AI course
=======
# Mancala AI Project

This project is a command-line simulation and gameplay implementation of the Mancala board game, featuring both human and AI players. It was developed as a final project for an AI course to explore search algorithms like Minimax and Alpha-Beta Pruning, as well as evaluate advanced heuristic-based decision-making.

## Features

- Fully functional 2-player Mancala implementation (6 pits + 1 Mancala per side)
- Multiple AI agents with increasing levels of sophistication:
  - `RandomPlayer` – chooses random valid moves
  - `MinimaxPlayer` – searches the game tree using the Minimax algorithm
  - `AlphaBetaPlayer` – optimized Minimax with Alpha-Beta pruning
  - `AdvancedAlphaBetaPlayer` – uses a custom evaluation function and deeper lookahead
- CLI-based human vs. AI and AI vs. Random simulations
- Performance statistics from batch simulations

## Project Structure

```
.
├── mancala.py           # CLI interface and human-AI gameplay loop
├── mancalaGame.py       # Core game logic and AI player implementations
├── simulator.py         # Tools for running and benchmarking AI simulations
├── README.md            # Project overview and instructions
```

## Getting Started

To play the game:

```bash
python mancala.py
```

Choose from the following gameplay modes:

1. Human vs Human  
2. Human vs Random AI  
3. Human vs Minimax AI  
4. Human vs Alpha-Beta AI  
5. Human vs Advanced Alpha-Beta AI  

To run AI simulations and see performance stats:

```bash
python simulator.py
```

Simulations include:
- Random vs Random
- Minimax vs Random
- Alpha-Beta vs Random
- Advanced Alpha-Beta (depth=10) vs Random

## Results Summary

| Matchup                            | Player 1 Win % | Player 2 Win % | Tie % | Avg Moves | Time/Game (s) |
|------------------------------------|----------------|----------------|--------|-----------|----------------|
| Random vs Random                   | 49%            | 48%            | 3%     | 41.58     | —              |
| Minimax (depth=5) vs Random        | 94%            | 5%             | 1%     | 29.47     | —              |
| Alpha-Beta (depth=5) vs Random     | 95%            | 3%             | 2%     | 29.09     | 0.02           |
| Advanced Alpha-Beta (depth=10)     | 96%            | 4%             | 0%     | 25.24     | 2.25           |

## Advanced Evaluation Heuristic

Original evaluation function:
```python
score = myMancala - oppMancala
```

AdvancedAlphaBetaPlayer evaluation function:
```python
score = (myMancala - oppMancala) + 0.4 * (sum(myPits) - sum(oppPits)) + endgameBonus
```

This function rewards:
- Higher Mancala score
- More stones on the board (pit control)
- Endgame advantage

## Learnings

- Implemented Minimax and Alpha-Beta pruning for turn-based decision making
- Created evaluation functions to influence strategic AI behavior
- Benchmarked AI performance using simulations
- Developed a modular and maintainable Python codebase

## Dependencies

- Python 3.6+
- No external libraries (uses only `random` and `time`)

## License

MIT License — free to use, modify, and distribute.

## Acknowledgements

This project was completed as a final assignment for the University of Colorado Boulder CSCI 3022 AI course. It explores fundamental decision-making algorithms applied in game AI.
>>>>>>> f4c668a (initial commit)
