# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

	1.	The New Game button is not working properly after the player wins the game
	2.	The Hard difficulty level is incorrectly set to a range of 1–50 instead of the expected 1–500
	3.	The attempt counter begins at 1 instead of correctly starting from 0

--- 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used GitHub Copilot in VS Code. I used both Agent Mode 
(to fix and refactor code across files) and Copilot Chat 
(to explain bugs and generate pytest tests).

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked Copilot to fix the check_guess function in logic_utils.py 
where the hints were reversed. Copilot correctly identified that 
the comparison logic was wrong and rewrote the function using 
the right greater than and less than operators. I verified this 
by running pytest and all 6 tests passed. I also manually tested 
it in the browser by guessing numbers higher and lower than the 
secret and the hints were correct.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I asked Copilot to generate a pytest test, it gave me the 
test code but did not include the import statement at the top 
of the file. When I ran pytest it gave me a ModuleNotFoundError. 
I had to manually add the import sys and sys.path.insert lines 
at the top of the test file to fix it. This showed me that 
Copilot's suggestions need to be carefully reviewed and tested 
before trusting them completely.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I used two ways to confirm a bug was fixed. First I ran pytest 
in the terminal to check that all the automated tests passed. 
Then I manually tested the game in the browser by playing it 
and checking that the hints and win condition behaved correctly.

- Describe at least one test you ran (manual or using pytest)  
I ran pytest after fixing the check_guess function in 
logic_utils.py. The test file had 3 tests — test_winning_guess, 
test_guess_too_high, and test_guess_too_low. Before the fix all 
3 tests failed with a NotImplementedError. After I filled in 
the correct logic all 3 tests passed. This told me that the 
function was correctly returning "Win", "Too High", and "Too Low" 
for the right inputs.

- Did AI help you design or understand any tests? How?
Yes. I asked Copilot Chat to generate a pytest test that checks 
check_guess returns "Too High" when the guess is 60 and the 
secret is 50. Copilot wrote the test function for me and I 
pasted it into test_game_logic.py. This helped me understand 
how pytest tests are structured — each test calls a function 
with specific inputs and uses assert to check the output is 
what we expect.


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
