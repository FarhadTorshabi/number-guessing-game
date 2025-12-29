# 🎯 Number Guessing Game (Python)

A console-based number guessing game written in Python.

This project was originally created while learning Python basics and was later **refactored** to improve code structure, readability, and logic separation.

---

## 🧠 What This Project Demonstrates

- Clean function design (single responsibility)
- Input validation and edge case handling
- Use of loops and conditionals
- Refactoring for readability and maintainability
- Basic game logic and user interaction

---

## 🎮 How the Game Works

1. The player chooses a difficulty level:
   - **Easy**: numbers 1–10 (5 attempts)
   - **Medium**: numbers 1–20 (4 attempts)
   - **Hard**: numbers 1–50 (3 attempts)
2. The program randomly selects a secret number.
3. The player guesses until:
   - The number is found
   - Attempts run out
   - The player quits by typing `q`
4. The game provides:
   - High / low feedback
   - Hot / cold hints
   - Best score tracking

---

## ▶️ How to Run

Make sure you have Python 3 installed.

```bash
python guess_number.py
