import tkinter as tk
from tkinter import ttk

window_width = 400
window_height = 600
header_bg ="red"
header_height = 100
body_height = 400
footer_height = 100

#funzioni
def write_word(word_index, word):
    for i in range(len(word)):
        str[int(word_index)][i].set(word[i])

def clean_panel():
    for i in range(5):
        for j in range(5):
            str[i][j].set("*")

window = tk.Tk()
window.title("Wordle Game")
x = int(window.winfo_screenwidth()/2 - (window_width/2))
y = int(window.winfo_screenheight() * 0.1)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.resizable(False, False)

#header section
header = tk.Frame(window, width=window_width, height=header_height, background=header_bg)
header.pack()

header_label = tk.Label(header, text="Wordle Game", font=("Arial", 25), background=header_bg)
header_label.pack()


#body section
body = tk.Frame(window, width=window_width, height=body_height, background="white")
body.pack()

body_frame = []
str = []
entry = []
for i in range(5):
    body_frame.append(tk.Frame(body, width=window_width, height=50,))
    body_frame[i].pack()
    body_frame[i].pack(pady=3, padx=10)
    str.append([])
    entry.append([])
    for j in range(5):
        str[i].append(tk.StringVar())
        str[i][j].set("*")
        entry[i].append(tk.Entry(body_frame[i], width=2, 
                            font=("Arial", 25), 
                            justify="center", 
                            disabledbackground="white",
                            disabledforeground="black", 
                            borderwidth=1, 
                            relief="solid",
                            textvariable=str[i][j],
                            state="disabled"))
        entry[i][j].pack(side="left")

write_word(0, "ciao!")
write_word(1, "cuore")
write_word(2, "muore")
write_word(3, "muore")
write_word(4, "muore")
clean_panel()

#footer section
footer = tk.Frame(window, width=window_width, height=footer_height, background="green")
footer.pack()

window.mainloop()
