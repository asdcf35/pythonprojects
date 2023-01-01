from tkinter import *
#
root = Tk()
root.title("Multidimensional Arrays")

root.geometry("500x500")
label = Label(root)

array = [
    [
        [
            "John",
            "A+",
            "Excellent",
        ],
        [
            "James",
            "A",
            "Very Good",
        ],
        [
            "Thomson",
            "B",
            "Good",
        ]
    ]
]

print(array[0][0][2])


def report():
    text = ""
    for i in range(len(array[0])):
        text += f"{array[0][i][0]} got grade {array[0][i][1]} and he is doing {array[0][i][2]}\n\n"
    label["text"] = text


btn = Button(root, text="show report", command=report)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
