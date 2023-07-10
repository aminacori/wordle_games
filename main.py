import tkinter as tk
from tkinter import ttk
import random

window_width = 400
window_height = 600
header_bg ="#00a6fb"
header_height = 100
body_height = 400
footer_height = 100
empty_char = " "

#funzioni

def evidenzia_lettera():
    for i in range(5):
        for j in range(5):
            entry[i][j].config(borderwidth=1)
    if index_letter < 5 and index_word < 5:
        entry[index_word][index_letter].config(borderwidth=3, highlightbackground="white")
    elif index_letter >= 5:
        entry[index_word][4].config(borderwidth=3, highlightbackground="white")

def write_word(word_index, word):
    for i in range(len(word)):
        str[int(word_index)][i].set(word[i].upper())

def write_letter(word_index, letter_index, letter):
    str[int(word_index)][int(letter_index)].set(letter.upper())

def clean_panel():
    for i in range(5):
        for j in range(5):
            str[i][j].set(empty_char)
    globals()['index_letter'] = 0
    globals()['index_word'] = 0

def text_style_gray(i,j):
    entry[i][j].config(disabledforeground="white")
    entry[i][j].config(disabledbackground="gray")

def text_style_green(i,j):
    entry[i][j].config(disabledforeground="white")
    entry[i][j].config(disabledbackground="green")

def text_style_orange(i,j):
    entry[i][j].config(disabledforeground="white")
    entry[i][j].config(disabledbackground="orange")

def keypress_event(event):
    print("Hai premuto:" + event.char )
    if event.char.isalpha() and globals()['index_letter'] < 5:
        write_letter(globals()['index_word'], globals()['index_letter'], event.char)
        globals()['index_letter'] += 1
    evidenzia_lettera()

def returnpress_event(event):
    print("Hai premuto: Invio")
    if globals()['index_letter'] == 5:
        check_word()
    evidenzia_lettera()
    

def backspace_event(event):
    print("Hai premuto: Backspace")
    if globals()['index_letter'] > 0:
        globals()['index_letter'] -= 1
        str[globals()['index_word']][globals()['index_letter']].set(empty_char)
    evidenzia_lettera()

def check_word():
    word = ""
    for i in range(5):
        word += str[globals()['index_word']][i].get()
    print("La parola inserita è "+word)
    if word == globals()['secret_word'].upper():
        print("Hai vinto")
        for i in range(5):
            color_by_text("green", globals()['index_word'], i)
        
    elif globals()['index_word'] < 4:
        check_letter(word)
        print("Prossima riga")
        globals()['index_word'] += 1
        globals()['index_letter'] = 0
    else:
        check_letter(word)
        print("Hai perso")

def color_by_text(color, i, j):
    if color == "gray":
        text_style_gray(i,j)
    elif color == "green":
        text_style_green(i,j)
    elif color == "orange":
        text_style_orange(i,j)

def check_letter(word):
    lista_lettere = ["gray", "gray", "gray", "gray", "gray"]
    s_word = globals()['secret_word'].upper()
    word.upper()
    print(s_word)
    print(word)
    for i in range(5):
        if s_word[i] == word[i]:
            lista_lettere[i] = "green"
        elif word[i] in s_word:
            lista_lettere[i] = "orange"
            globals()['secret_word'][i].lower()
    for i in range(5):
        color_by_text(lista_lettere[i], globals()['index_word'], i)
    



# definisco gli indici di parole e lettera
index_word = 0
index_letter = 0

# definisco le parole da giocare
words = ["amore", "mondo", "cuore", "pesce"]
# secret_word = words[random.randint(0,len(words)-1)]
secret_word = "amore"

window = tk.Tk()
window.title("Wordle Game")
window.config(background=header_bg)
x = int(window.winfo_screenwidth()/2 - (window_width/2))
y = int(window.winfo_screenheight() * 0.1)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.resizable(False, False)
window.bind("<Key>", lambda event: keypress_event(event))
window.bind("<Return>", lambda event: returnpress_event(event))
window.bind("<BackSpace>", lambda event: backspace_event(event))

#funzione per il tasto backspace

#header section
header = tk.Frame(window, width=window_width, height=header_height, background="#00FFFF")
header.pack(pady=10)

header_label = tk.Label(header, text="Wordle Game", font=("Arial", 32, "bold"), background=header_bg, foreground="white")
header_label.pack()


#body section
body = tk.Frame(window, width=window_width, height=body_height, background="white")
body.pack(pady=10)

body_head_frame = tk.Frame(body, width=window_width, height=20, background="white")
body_head_frame.pack()

body_frame = []
str = []
entry = []
for i in range(5):
    body_frame.append(tk.Frame(body, width=window_width, height=50, background="white"))
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
        entry[i][j].pack(side="left", padx=2)

body_bottom_frame = tk.Frame(body, width=window_width, height=20, background="white")
body_bottom_frame.pack()

# write_word(0, "Amore")
# text_style_gray(0,0)
# text_style_green(0,1)
# text_style_orange(0,2)
evidenzia_lettera()

#footer section
footer = tk.Frame(window, width=window_width, height=footer_height, background="white")
footer.pack()
label_messaggi = tk.Label(footer, 
                          width=window_width,
                          text="Benvenuto nel gioco di Wordle. \nInserisci la parola da 5 lettere e premi invio per confermare!", 
                          font=("Arial", 11), 
                          background="white")
label_messaggi.pack(pady=10)

window.mainloop()
