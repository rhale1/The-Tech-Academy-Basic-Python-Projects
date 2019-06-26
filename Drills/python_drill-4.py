#
# Python: 3.7.3
#
# Author: Rachel Hale
#
# Purpose: The Tech Academy - Python Course
#For this drill, you will need to write a script that creates a GUI with a button widget and a text widget.
#Your script will also include a function that when it is called will invoke a dialog modal which will allow
#users with the ability to select a folder directory from their system. Finally, your script will show the user’s
#selected directory path into the text field.
#
from tkinter import * 
from tkinter import messagebox, filedialog

root = Tk(screenName=None, baseName=None, className='Simple Find File', useTk=1)

def findFile():
    fileName = filedialog.askdirectory()
    entry=Entry(root)
    entry.grid(row=3, column=1, padx = 10)
    Button(root,text="View Path...", command=lambda:entry.insert(END,fileName)).grid(row=2, column=1, padx=10, pady=5, ipadx=19)

Button(root,text="Select File...", command=findFile).grid(row=1, column=1, padx=10, pady=5, ipadx=19)

root.mainloop ()

