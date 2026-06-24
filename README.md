# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

The game is a number guessing game where the player tries to guess a secret number within a limited number of attempts. The difficulty setting controls the range and attempt limit.

Bugs I found:
- The hint messages were backwards — guessing too high told you to go higher instead of lower
- On every even attempt, the secret number was converted to a string, breaking number comparisons
- The Hard difficulty range (1-50) was actually easier than Normal (1-100)
- The score incorrectly rewarded wrong "Too High" guesses on even attempts

Fixes I applied:
- Swapped the hint messages in check_guess so they correctly say "Go LOWER" and "Go HIGHER"
- Removed the string conversion so the secret always stays an integer
- Refactored check_guess into logic_utils.py where game logic belongs


## 📸 Demo Walkthrough

1. User selects "Normal" difficulty (range 1-100, 8 attempts allowed)
2. Game generates a secret number (e.g. 63)
3. User enters a guess of 40 — game returns "Too Low"
4. User enters a guess of 80 — game returns "Too High"
5. User enters a guess of 63 — game returns "Correct!"
6. Score updates correctly after each guess based on attempt number
7. Game ends and displays final score


## 🧪 Test Results

PS C:\Users\anang\ai110-module1show-gameglitchinvestigator-starter> python -m pytest tests/test_game_logic.py -v
============================================= test session starts ==============================================
platform win32 -- Python 3.13.2, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\anang\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\anang\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.9.0
collected 7 items                                                                                               

tests/test_game_logic.py::test_winning_guess PASSED                                                       [ 14%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                      [ 28%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                       [ 42%]
tests/test_game_logic.py::test_hint_too_high_message PASSED                                               [ 57%]
tests/test_game_logic.py::test_secret_always_integer PASSED                                               [ 71%]
tests/test_game_logic.py::test_secret_not_converted_to_string PASSED                                      [ 85%]
tests/test_game_logic.py::test_even_attempt_secret_is_integer PASSED                                      [100%]

============================================== 7 passed in 0.03s ===============================================
PS C:\Users\anang\ai110-module1show-gameglitchinvestigator-starter> 

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
