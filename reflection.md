# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game looked relatively simple and easy to navigate. It had three levels- easy, normal and hard. I had to enter a number between 1-100 and guess what the number was before the attempts ran out. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. the score kept decreasing and was shown in negative, instead of resetting to 0.
  2. the hint suggests only going lower, even at lower numbers like 0 and 1.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Copilot

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  When I asked Copilot for bugs in the code, it suggested a couple of them including the new game button which didn't fully reset the game. I verified this was right by trying the feature out on the app. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  When I asked AI to fix the bug, it created another file instead of editing the existing ones.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

<!-- Diagnostic notes: locate the score bug -->
- Location of the score bug (diagnostic):
  The negative-score behavior is caused by state handling in the Streamlit app file:
  - File: /Users/yaminikattelu/codepath/ai110-module1show-gameglitchinvestigator-starter/streamlit_app.py
  - Inspect these places:
    1. App start / session_state initialization: make sure 'score' is initialized, e.g.
       if 'score' not in st.session_state: st.session_state['score'] = 0
    2. reset_game (new game handler): ensure it sets st.session_state['score'] = 0 and reinitializes other game keys.
    3. Guess handling (where score is decremented): replace raw decrement with a clamp, e.g.
       st.session_state['score'] = max(0, st.session_state.get('score', 0) - 1)
    4. New Game button: ensure it calls the reset function (st.button(..., on_click=reset_game) or call reset_game() on press).
  - These minimal edits will stop the score from going negative and ensure it resets to 0 on a new game.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?
  I added a dedicated reset function that initializes all relevant session_state keys when starting a new game (including secret_number and score). I also clamped the score when decrementing so it never goes below 0 (using max(0, ...)), and ensured the New Game button invokes the reset function so the game state is fully reset.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
