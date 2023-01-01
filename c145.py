from tkinter import *
root = Tk()

root.title("Addition")
root.geometry("400x200")


show_result = Label(root)
def add():
    show_result['text'] = 4 + 1
    return None

btn = Button(root, text="Add", command=add)

btn.pack()

show_result.pack()

root.mainloop()