from tkinter import *

root = Tk()
elements = []
root.title("Fibonacci")
root.geometry("400x400")

series = Label(root, text="Fibonacci Series...")
flower = Label(root)
spiral = Label(root)
fiboSum = Label(root)
elements.append(series)
elements.append(flower)
elements.append(spiral)
elements.append(fiboSum)

def Fibonacci():
    nums: list = [0,1]
    for i in range(8):
        nums.append(nums[-1] + nums[-2])
    flower['text']: str = 'Flower is fully bloomed'
    spiral['text']: str = f'Spirals in the right direction are: {nums[-1]} \n Spirals in the left direction are: {nums[-2]}\n Total number of spirals: {nums[-1]+nums[-2]}'
    print(nums)
    fiboSum['text']: str = f"Fibonacci Sum: {sum(nums)}"
    return None

btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)
elements.append(btn)

for element in elements:
    element.pack()

root.mainloop()
