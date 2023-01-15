from customtkinter import *
from random import *
set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = CTk(fg_color="yellow")
root.geometry("400x400")

label = CTkLabel(root, text="", text_color="black")

def word_random() -> str:
    return "".join([chr(randint(ord("a"), ord("z"))) for i in range(6)])

button = CTkButton(root, text="Generate Random Word", command=lambda : label.configure(text=word_random()))

button.place(relx=0.5, rely=0.4, anchor=CENTER)
label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
