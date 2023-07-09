import tkinter as tk
from tkinter import ttk

window_width = 400
window_height = 600
header_bg ="red"
header_height = 100
body_height = 400
footer_height = 100
empty_char = " "

#funzioni
def write_word(word_index, word):
    for i in range(len(word)):
        #convetto word[i] in uppercase
        str[int(word_index)][i].set(word[i].upper())

def clean_panel():
    for i in range(5):
        for j in range(5):
            str[i][j].set(empty_char)

def text_style_gray(i,j):
    entry[i][j].config(disabledforeground="white")
    entry[i][j].config(disabledbackground="gray")

def text_style_green(i,j):
    entry[i][j].config(disabledforeground="white")
    entry[i][j].config(disabledbackground="green")

def text_style_orange(i,j):
    entry[i][j].config(disabledforeground="white")
    entry[i][j].config(disabledbackground="orange")

window = tk.Tk()
window.title("Wordle Game")
x = int(window.winfo_screenwidth()/2 - (window_width/2))
y = int(window.winfo_screenheight() * 0.1)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.resizable(False, False)

#header section
header = tk.Frame(window, width=window_width, height=header_height, background=header_bg)
header.pack(pady=20)

header_label = tk.Label(header, text="Wordle Game", font=("Arial", 32, "bold"))
header_label.pack()


#body section
body = tk.Frame(window, width=window_width, height=body_height, background="white")
body.pack(pady=10)

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
        str[i][j].set(empty_char)
        entry[i].append(tk.Entry(body_frame[i], width=2, 
                            font=("Arial", 25, "bold"), 
                            justify="center", 
                            disabledbackground="white",
                            disabledforeground="black", 
                            borderwidth=1, 
                            relief="solid",
                            textvariable=str[i][j],
                            state="disabled"))
        entry[i][j].pack(side="left")

write_word(0, "Amore")
text_style_gray(0,0)
text_style_green(0,1)
text_style_orange(0,2)


#footer section
footer = tk.Frame(window, width=window_width, height=footer_height, background="green")
footer.pack()

window.mainloop()
