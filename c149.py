from tkinter import *
import random

root = Tk("Luck Friend Wheel")
root.geometry("500x500")

friendList: list = ["James", "Isabella", "Sophia", "Oliver", "Peter"]
_ = None
print(friendList)


def randomFriend() -> None:
    _: int = random.randint(0, len(friendList))
    numLabel["text"] = _
    lucky_friend["text"] = f"Your lucky friend is {friendList[_]}"


def addFriend() -> None:
    ndf = name.get()
    if ndf not in friendList:
        friendList.append(ndf)
    friend_list["text"] = "Your friend list: " + str(friendList)


name = Entry(root)
name.place(relx=0.5, rely=0.2, anchor=CENTER)

btn1 = Button(root, text="Add to friend list", command=addFriend)
btn1.place(relx=0.5, rely=0.3, anchor=CENTER)

friend_list = Label(root)
friend_list["text"] = "Your friend list: " + str(friendList)
friend_list.place(relx=0.5, rely=0.4, anchor=CENTER)

numLabel = Label(root)
numLabel["text"] = _
numLabel.place(relx=0.5, rely=0.6, anchor=CENTER)

lucky_friend = Label(root)
lucky_friend.place(relx=0.5, rely=0.7, anchor=CENTER)

btn = Button(root, text="Who is your lucky friend?", command=randomFriend)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
