# 0x0A. Prime Game

## Overview
This project implements a prime number-based game algorithm where two players (Maria and Ben) take turns choosing prime numbers and their multiples from a set of consecutive integers. The project is part of the ALX Interview Preparation curriculum.


## Project Description
The game consists of players (Maria and Ben) taking turns choosing a prime number from a set of consecutive integers starting from 1 up to and including n. The chosen prime number and its multiples are then removed from the set. The player who cannot make a move loses the game.

### Game Rules
1. The game starts with a set of consecutive integers from 1 to n
2. Maria always plays first
3. Both players play optimally
4. Each player takes turns picking a prime number and removing its multiples
5. The game ends when no prime numbers remain
6. The player who cannot make a move loses

## Requirements

### General
- **Allowed editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS
- **Python Version**: Python 3.4.3
- **Style Guide**: PEP 8 (version 1.7.x)
- **File Structure**:
  - All files should end with a new line
  - First line must be `#!/usr/bin/python3`
  - All files must be executable

### Technical Requirements
- No external packages can be imported
- Maximum value for n and x: 10000

## Function Prototype
```python
def isWinner(x, nums)
```

...
