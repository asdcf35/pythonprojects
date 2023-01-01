from tkinter import *
import random
# Basic tkinter template
elements = []
root = Tk()
root.configure()
canvas=Canvas(root,width=400,height=45)
root.geometry()
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")
label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
elements.append(canvas);
def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
 
    return "key doesn't exist"
#templates
templates = {}
templates["licenseID"]: str = f"ID: {random.randint(1_000_000_000, 9_999_999_999)}"
templates["personName"]: str = "Name: John Doe"
templates["dateOfBirth"]: str = f"Date of Birth: {random.randint(1,12)}/{random.randint(1,20)}/{random.randint(1900, 1999)}"
templates["PIN"]: str = f"PIN #: {random.randint(1_000_000_000, 9_999_999_999)}"
templates["address"]: str = "Address: 1 Apple Way, Oakland, MD"
templates["typeOfVehicle"]: str = "Authorization to drive the following vehicles: Car, Motorcycle, Plane "

#label
labels = {}
labels["licenseID"] = Label(root)
labels["personName"] = Label(root)
labels["dateOfBirth"] = Label(root)
labels["PIN"] = Label(root)
labels["address"] = Label(root)
labels["typeOfVehicle"] =  Label(root)

#
for label in labels:
  labels[label]["text"] = templates[label]
  elements.append(labels[label])

#final pack
for element in elements:
    element.pack()

root.mainloop();
