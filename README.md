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

- [ ] Describe the game's purpose.
The game picks a random secret number and the player guesses it.
After each guess the game gives a hint to guide the player 
higher or lower. The goal is to guess the correct number in 
as few attempts as possible.

- [ ] Detail which bugs you found.
Bug 1: The New Game button was not working properly after the 
player wins the game. It was not resetting the game state 
correctly so the player could not start a fresh game after winning.

Bug 2: The Hard difficulty level was incorrectly set to a range 
of 1–50 instead of the expected range of 1–500. This meant Hard 
mode was easier than intended.

Bug 3: The Enter button was not working. The player had to 
manually click Submit every time. Expected behavior is that 
pressing Enter should also submit the guess.

- [ ] Explain what fixes you applied.
Bug 1: I used GitHub Copilot Agent Mode to fix the New Game 
button logic so it correctly resets the game state after a win.

Bug 2: I corrected the Hard difficulty range from 1–50 to 1–500 
in the code. I verified both fixes by manually testing the game 
in the browser and running pytest — all 6 tests passed.

Bug 3 Fix: I used Claude in VS Code to fix the Enter button. 
I verified by running the game in the browser and pressing 
Enter after typing a guess — it now submits correctly.



## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
