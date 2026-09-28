# 🎮 Game Glitch Investigator: The Impossible Guesser
Submitted by: Syeda Farwa Rizvi - AI110-3
## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.

A guessing game, to guess a secret number and keep track of score for how many times the guess was right, if attempts not used up.


### Bugs I found
1. the hints are opposite. If the secret number is higher than guessed number, it should say Go higher, instead it says go lower, and vice versa.
2. The game does not let you start a new game. When new game pressed, it never lets you submit a guess. 
3. Not being able to start a new game means the score will never update.
4. The score displayed and score in debugger info dont match, have a 10 point difference, but starting new game stores the displayed score.
5. Changing the difficulty doesn't make sense; easy has fewer attempts than normal, and the secret number is the same.

#### Bugs my AI Assistant helped me find:
6. Guesses silently compared as text on every even attempt — app.py:158-161: on even-numbered attempts, secret is converted to a string before calling check_guess. Comparing int > str raises TypeError, which the except block in check_guess catches by comparing the string representations instead (logic_utils.py:41-47). String comparison is lexicographic, not numeric; e.g. guessing 9 against secret 10 says "Too High" (should be "Too Low") because "9" > "10" as text. This silently corrupts roughly half of all guesses.
7. Contradictory scoring for the same mistake — logic_utils.py:57-60: a "Too High" guess gives +5 points on even attempts but -5 on odd attempts, while "Too Low" always gives -5. Being wrong is randomly rewarded depending on attempt parity.
8. Attempts start inconsistently — session init sets attempts = 1 (app.py:96), but New Game resets it to 0 (app.py:135). This mismatch also means your very first guess of the very first game already lands on an "even" attempt count, triggering bug #6 immediately rather than "every other guess."
9. Off-by-one on attempt limit — because attempts starts at 1 and increments before the >= attempt_limit check (app.py:182), you actually only get attempt_limit - 1 real guesses, not the number shown in the sidebar.
10. Wrong range shown in the guess prompt — app.py:109-112 always says "Guess a number between 1 and 100," even on Easy (1-20) or Hard (1-50).
11. The refactor to logic_utils.py was never done — every function there (logic_utils.py:1-26) is still a stub that just raises NotImplementedError; app.py keeps its own inline duplicates instead of importing them. That means tests/test_game_logic.py currently fails outright. Separately, once someone does move the code over, the tests expect check_guess to return a plain string like "Win" (tests/test_game_logic.py:6), but the actual function returns a tuple (outcome, message) — so the tests won't pass even after refactoring, without also updating them or the function.

### [ ] Explaination of fixes I applied.
1. Hints fix: the hints were opposite of what they were supposed to be, so, I reversed the arithmetic operation and corrected the issue.
2. The game does not let you start a new game. When new game pressed, it never lets you submit a guess.  For this, I reset the history to an empty list, status updated to "playing" and parameters of secret number to low, high

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
