'''
This is the main file of the hashed password cracker tool.
It provides a user-friendly interface for inputting hashed passwords and initiates the cracking process.
'''
import tkinter as tk
from password_cracker import PasswordCracker
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hashed Password Cracker")
        self.geometry("400x200")
        self.label = tk.Label(self, text="Enter hashed password:")
        self.label.pack()
        self.entry = tk.Entry(self, show="*")
        self.entry.pack()
        self.button = tk.Button(self, text="Crack Password", command=self.crack_password)
        self.button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
    def crack_password(self):
        hashed_password = self.entry.get()
        password_cracker = PasswordCracker()
        result = password_cracker.crack(hashed_password)
        self.result_label.config(text=result)
if __name__ == "__main__":
    app = Application()
    app.mainloop()