import tkinter as tk
from tkinter import messagebox
import random
import string
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg="yellow")
        # Widgets
        self.title_label = tk.Label(root, text="PASSWORD GENERATOR", font=("Comic Sans MS", 18, "bold"), fg="black", bg="yellow")
        self.length_label = tk.Label(root, text="Enter length of the password:", font=("Arial", 12,"bold"), fg="black", bg="yellow")
        self.length_entry = tk.Entry(root, font=("Arial", 12))
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Arial", 12), fg="yellow", bg="black")
        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="black", bg="yellow")
        # Widget Placement
        self.title_label.pack(pady=10)
        self.length_label.pack(pady=10)
        self.length_entry.pack(pady=10)
        self.generate_button.pack(pady=20)
        self.result_label.pack()
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                messagebox.showerror("Error", "Password length should be at least 4 characters.")
                return
            password = self._generate_password(length)
            self.result_label.config(text=f"Generated Password: {password}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
    def _generate_password(self, length):
        num_letters = length // 2
        num_digits = random.randint(1, length - 2)
        num_symbols = length - num_letters - num_digits
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
        password = (
            ''.join(random.choice(letters) for _ in range(num_letters)) +
            ''.join(random.choice(digits) for _ in range(num_digits)) +
            ''.join(random.choice(symbols) for _ in range(num_symbols))
        )
        password_list = list(password)
        random.shuffle(password_list)
        shuffled_password = ''.join(password_list)
        return shuffled_password
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
