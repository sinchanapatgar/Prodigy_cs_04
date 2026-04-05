⌨️ PRODIGY_CS_04 – Simple Keylogger
Prodigy Infotech Cybersecurity Internship – Task 04
📌 Overview
A Python GUI application that records and logs keystrokes with timestamps to a log file. Built for educational purposes to understand how keyloggers work and the importance of cybersecurity awareness.
⚠️ Ethical Notice: This tool is strictly for educational purposes. Only use it on your own device with full knowledge and consent. Keylogging without explicit permission is illegal and unethical.
🖥️ Features
▶️ Start / ⏹ Stop logging controls
Logs all keystrokes with timestamps to keylog.txt
Handles special keys: Enter, Space, Backspace, Tab, Ctrl, Shift, Alt, etc.
Live log display in the GUI window
Keystroke counter
Clear log button
Dark-themed GUI built with Tkinter
🧠 How It Works
The program uses the pynput library to listen for keyboard events. When a key is pressed:
The key character or special key name is captured
A timestamp is added
The entry is written to keylog.txt
The entry is displayed in the GUI live log
Example log output (keylog.txt):
========================================
▶ Logging started at 2024-01-15 10:30:00
========================================
[10:30:01] H
[10:30:01] e
[10:30:01] l
[10:30:01] l
[10:30:01] o
[10:30:02] [SPACE]
[10:30:02] W
[10:30:03] [ENTER]
⏹ Logging stopped at 10:30:05
🚀 How to Run
Prerequisites
Python 3.8+
Install pynput:
pip install pynput
Run the Program
python PRODIGY_CS_04.py
🖼️ Usage
Launch the application
Click ▶ START LOGGING to begin capturing keystrokes
Type anywhere on your keyboard — keystrokes appear in the live log
Click ⏹ STOP to end logging
Find the complete log in keylog.txt in the same directory
Click 🗑 CLEAR to clear the display
📁 File Structure
PRODIGY_CS_04/
├── PRODIGY_CS_04.py   # Main program
├── keylog.txt         # Generated log file (created on first run)
├── requirements.txt   # Dependencies
└── README.md          # Documentation
🛠️ Tech Stack
Tool
Purpose
Python 3
Core language
tkinter
GUI framework
pynput
Keyboard listener
datetime
Timestamp generation
⚠️ Legal & Ethical Disclaimer
Use only on your own computer
Never deploy on another person's device without their explicit written consent
This project is for learning purposes only — to understand how keyloggers function and how to defend against them
The developer is not responsible for any misuse of this code
