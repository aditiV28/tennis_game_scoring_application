# Tennis game scoring application

# Objective

Create a Python application that returns the verbal result of a tennis game given two Player objects representing the server and receiver.


# Approach Used

# 1. Modular Design
- `main.py` : Contains the input from command line interface, performs data validation on the input and returns the score.
- `utils.py` :  Contains the helper functions, custom exceptions and logic for input(name and score) validation.
- `Player` : Creates a simple @dataclass to hold the Player name and score.

# 2. Input Validations
- Player Name : Checks for length, allowed characters (letters, spaces, hyphens, apostrophes), and non-emptiness.
- Player Score : Must be a non-negative integer.
- Additional error handling checks:
  - Negative scores -> `NegativeTennisScoreException`
  - Both players have 0 -> `NoScoreAtStartOfGameException`
  - Win margin > 2 -> `WonByTooManyPointsException`
  - Invalid Name -> `InvalidNameException`

# 3. Scoring Logic
Implemented in `get_tennis_score()` with helper functions:
- `_is_draw()`
- `_is_deuce()`
- `_is_pre_deuce()`

**These helper fucntions minimize nesting and increase readability.**

# 4. CLI Input
- Using `input()` wrapped in `try/except` to ensure type safety.
- Score inputs cast to `int`.


# Assumptions Made

- Player names can include alphabets, spaces, hyphens and apostrophe.
- Player names cannot be empty and longer than 25 characters.
- Valid score values range from 0 upwards, as per tennis rules.
- Score announcements aren't made when both scores are 0.
- Score difference between two Players cannot be 2
- Scores cannot be a negative number

---

# Tools & Best Practices

- Code follows **PEP8** using tools like **Ruff**.
- Input validation is being done using `try-except`.
- Code is modularised by moving helper functions to a separate `utils.py` file, thus improving testability, readability and  maintainability.
- Variables are clearly named therefore indicating what value they hold.
- Typing is used throughout the code, clearly mentioning the expected input datatype and datatype of output returned.

---

# Files

- `main.py` – CLI logic and app entry point.
- `utils.py` – Helper functions and custom exceptions.
- `README.md` – This document containing a brief explanation of approach used, tools, best practices and assumptions made.