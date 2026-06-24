# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
--Answer:  It looked like a pretty decent prediction game where user will guess the number between the given range.

- List at least two concrete bugs you noticed at the start  
 --The hints were opposite, "Go Higher" showed when my guess was too high
 --The Hard difficulty range (1–50) was easier than Normal (1–100), which is the opposite of what "Hard" should mean

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 40, secret is 30  |  Hint: "Too High" / "Go Lower" | Hint: "Go HIGHER!" (backwards) | None |
|  Select "Hard" difficulty | Smaller range = harder (e.g. 1–200)|Range is 1–50, easier than Normal's 1–100 |None  |
| -1 |number out of range |Took the input |None |


---

## 2. How did you use AI as a teammate?

I used Claude in VS Code as my main AI assistant for this project.

Correct AI suggestion: fixing the backwards hints:**
The AI correctly identified that the hint messages in check_guess were swapped and moved the fixed version into logic_utils.py. I verified this by running the game, checking the secret number in Developer Debug Info, and confirming the hints matched my guesses correctly. The pytest tests also confirmed the fix passed.

Incorrect AI suggestion: starter test assertions:**
The AI generated starter tests that asserted against a plain string like "Win", but check_guess actually returns a tuple like ("Win", "Correct!"). I caught this when pytest failed with AssertionError showing the full tuple. I had to prompt the AI again to fix the assertions to use result[0] instead.

---

---

## 3. Debugging and testing your fixes

For Bug 1, I ran pytest and confirmed test_guess_too_high and test_hint_too_high_message both passed, then manually tested in the browser to make sure the hints matched the actual secret number. For Bug 2, I ran test_secret_not_converted_to_string which specifically checks that integer comparison still works correctly after removing the str() conversion. I also opened app.py to visually confirm the broken string conversion lines were completely gone and replaced with a single line.

---

## 4. What did you learn about Streamlit and state?

- Streamlit reruns the entire Python script from top to bottom every time the user interacts with the page, like clicking a button or typing in a box. This means normal variables reset to their original values on every rerun. Session state is a dictionary that Streamlit keeps alive between reruns, so anything stored in st.session_state persists across interactions. Without session state, the secret number would change on every button click, making the game impossible to win.


## 5. Looking ahead: your developer habits

- One habit I want to carry forward is always running pytest after every fix, not just at the end. It caught the tuple assertion bug in the starter tests immediately, which I would have missed if I only tested manually. Next time I work with AI on a coding task, I would read the generated code more carefully before accepting it instead of just running it and seeing what breaks. This project showed me that AI generated code can look correct at first glance but have subtle logic bugs baked in, so treating it as a starting point rather than a finished solution is the right mindset.