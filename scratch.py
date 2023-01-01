from customtkinter import *
import random

set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = CTk()
root.title("Password Generator")
root.geometry("400x400")

label = CTkLabel(root)
array3d = [[str(i) for i in range(1, 7)]] + [["Head", "Tail"]] + [[chr(ord("a") + i) for i in range(8)]]


def new_password() -> None:
    label.configure(text=array3d[0][random.randint(0, len(array3d[0]) - 1)]
                         + "" + array3d[1][random.randint(0, len(array3d[1]) - 1)] +
                         "" + array3d[2][random.randint(0, len(array3d[2]) - 1)])
    return None


print(array3d)
btn = CTkButton(root, text="New Password", command=new_password)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
