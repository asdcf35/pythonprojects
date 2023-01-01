# -*- coding: utf-8 -*-
import tkinter as tk
import random as r

root = tk.Tk()
root.title("List")
root.geometry("400x400")

labels = {}
labels["numList"] = tk.Label(root)
labels["numListSorted"] = tk.Label(root)

def randomlist() -> None:
    numList = r.sample(range(10,30),5)
    labels["numList"]['text'] = f"Random List: {str(numList)}"
    labels["numListSorted"]['text'] = f"Sorted List: {sorted(numList)}"

btn = tk.Button(root,text="Generate Random List", command=randomlist)

btn.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

labels['numList'].place(relx=0.5, rely=0.5, anchor=tk.CENTER)
labels['numListSorted'].place(relx=0.5, rely=0.6, anchor=tk.CENTER)

root.mainloop()
