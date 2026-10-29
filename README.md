# 🔐 Python Password Checker

## 📌 Description
The **Python Password Checker** is a simple cybersecurity project developed using Python to evaluate password composition based on different character types. It analyzes a password by counting lowercase letters, uppercase letters, numeric digits, whitespace characters, and special characters to calculate a basic strength score.

This project demonstrates fundamental Python programming concepts, including conditional statements, loops, functions, string manipulation, and secure password input using the built-in `getpass` module.

## ✨ Features
- 🔡 Counts lowercase and uppercase letters.
- 🔢 Counts numeric characters.
- 🔣 Identifies special characters and whitespace.
- 📊 Calculates a basic password composition score.
- 💡 Provides feedback based on character variety.
- 🔒 Hides password input in supported terminals.
- 🔁 Allows users to check multiple passwords in one session.

## 🛠️ Technologies Used
- **Language:** Python
- **Modules:** `string`, `getpass`
- **Version Control:** Git and GitHub

## 🎯 Project Objective
The objective of this project is to understand basic password security concepts and develop a command-line tool that helps users evaluate password composition and recognize opportunities to improve password quality.

## ⚙️ How It Works
1. The user chooses whether to check a password.
2. The program securely prompts for password input using `getpass`.
3. It counts the different character categories.
4. It calculates a score based on the presence of those categories.
5. It displays the results and a feedback message.
6. The user can check another password or exit.

## 🚀 How to Run
1. Install Python 3.
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/password-checker-python.git
   ```
3. Navigate to the project directory:
   ```bash
   cd password-checker-python
   ```
4. Run the program:
   ```bash
   python password_checker.py
   ```

## 📚 Learning Outcomes
- Practiced Python functions, loops, and conditional statements.
- Learned basic string processing and character classification.
- Explored password composition and security awareness.
- Used Git and GitHub for source-code management.

## ⚠️ Limitations
This project uses a basic character-variety scoring method. It does not determine whether a password is common, predictable, reused, or resistant to modern password-guessing attacks. A higher score does not guarantee a secure password.

## 🔮 Future Improvements
- Add password-length evaluation.
- Detect common and easily guessed passwords.
- Integrate a password-strength estimation library.
- Add a graphical user interface.
- Provide recommendations for creating stronger, unique passwords.

## 👨‍💻 Author
Developed as a beginner-friendly Python cybersecurity project.
