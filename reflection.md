# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?


was not making any sense, and wouldnt let me play again


- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. the hints are opposite. If the secret number is higher than guessed number, it should say Go higher, instead it says go lower, and vice versa.
2. The game does not let you start a new game. When new game pressed, it never lets you submit a guess. 
3. Not being able to start a new game means the score will never update.
4. The score displayed and score in debugger info dont match, have a 10 point difference, but starting new game stores the displayed score.
5. Changing the difficulty doesn't make sense; easy has fewer attempts than normal, and the secret number is the same.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|20 |Go lower |Go Higher | |
| New Game Pressed| new guess|not submittable guess | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Used Claude Code.


- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

Mentioning all the bugs that i missed because i didnt test all my edge cases properly, and also helping me fix my second bug.

- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

It suggested additional changes to the new game fix i made, and since my aim was to focus on that one fucntion, i didnt accept it as it was out of scope.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I tested the cases on the app myself to identify the fix. And tested out the test cases also.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I tested out the hint fix. And it worked manually, as well as by pytest, however, it didnt work when odd numbers were involved.

- Did AI help you design or understand any tests? How?

It helped check my first bug, hint logic fix, to recommend going higher instead of going lower.

It used regression test for the reverse hint bug

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

it is a platform that helps display the web app and re runs in a way that is restarts. The session state is what tells us which phase the app is in at that point.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

I would want to get aid from AI by finding issues but would like to attempt fixes myself


- What is one thing you would do differently next time you work with AI on a coding task?

explore the streamlit app by all use and edge cases first

- In one or two sentences, describe how this project changed the way you think about AI generated code.

It is definetly not dependable for an end to end solution, a thorough understanding of how the AI is processing and executing tasks  is crucial. But it is also a goo peer reviewer of your code as you go.