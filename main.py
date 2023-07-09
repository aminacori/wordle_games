import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Wordle Game")
x = int(window.winfo_screenwidth()/2 - 200)
y = int(window.winfo_screenheight() * 0.1)
window.geometry(f"400x600+{x}+{y}")
window.resizable(False, False)




window.mainloop()
