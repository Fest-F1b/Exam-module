from tkinter import *
from tkinter import ttk
from tkinter import Tk
 
root = Tk()
root.title("Welcome")
root.geometry("400x400")

#registration with names use entry
username = Label(root, text = "Username", padx = 10)
username.grid(row = 0, column = 1)

my_entry = Entry(root)
my_entry.grid(row=2, column = 1)

#Age section use check boxes
age = Label(root, text = "Age", padx = 10)
age.grid(row =0, column = 2)
my_spinbox = Spinbox(
    root,
    from_=1,
    to=200,
    increment=1)
my_spinbox.grid(row =2, column = 2, padx = 10)  

#gender use check box (male and  Female)
gender = Label(root, text="Gender", padx=20)
gender.grid(row=3, column=1)
#male
male= Checkbutton(
    root, text="Male")
male.grid(row= 4, column= 1)
#female
female = Checkbutton(
    root, text="Female")
female.grid(row=4, column=2)

box = ttk.Combobox(
    root,
    values=["Option 1", "Option 2", "Option 3"])
box.grid(row = 6, column= 1,padx = 1)
def frame():

    secondf = LabelFrame(root, text="Welcome", borderwidth=1.5,
                        relief=GROOVE, highlightthickness=1, padx=20, pady=20)
    #secondf.grid(row = 5, column =2)
    
frame()    
   
root.mainloop()
