import tkinter as tk
from tkinter import simpledialog, messagebox
import time

# Set the time limit in seconds
TIME_LIMIT = 3600 # 1 hour

# Set the password
PASSWORD = "your_password"

class TimeLimitApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Time Limit")
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.start_time = time.time()
        self.after(1000, self.check_time_limit)
        self.popup = None

    def check_time_limit(self):
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= TIME_LIMIT:
            self.display_popup()
        else:
            self.after(1000, self.check_time_limit)

    def display_popup(self):
        if self.popup is None or not self.popup.winfo_exists():
            self.popup = tk.Toplevel(self)
            self.popup.title("Time Limit Reached")
            self.popup.grab_set()  # Make the popup window modal

            message_label = tk.Label(self.popup, text="It is recommended to take a break and shut down your computer for a while.", wraplength=300)
            message_label.pack(pady=10)

            close_button = tk.Button(self.popup, text="Close", command=self.reset_timer)
            close_button.pack(pady=5)

    def reset_timer(self):
        if self.popup:
            self.popup.destroy()
            self.popup = None
        self.start_time = time.time()
        self.after(1000, self.check_time_limit)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

if __name__ == "__main__":
    app = TimeLimitApp()
    app.mainloop()