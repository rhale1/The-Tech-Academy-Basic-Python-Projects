#
# Python: 3.7.4
#
# Author: Rachel Hale
#
# Purpose: The Tech Academy - Python Course, created GUI for a smaple window to check for files
#

from tkinter import * 

root = Tk()

#buttons
Button(root, bd=2, text="Browse...").grid(row=1, column=1, padx=10, pady=5, ipadx=19)
Button(root, bd=2, text="Browse...").grid(row=2, column=1, padx=10, pady=5, ipadx=19)
Button(root, text="Check for files...").grid(row=3, column=1, padx=10, pady=5, ipady=10)
Button(root, text="Close Program").grid(row=3, column=2, rowspan=1, padx=10, pady=5, ipady=10, sticky=E)

#text file
Entry(root, bd=2, width=50).grid(row=1, column=2, padx = 10)
Entry(root, bd=2, width=50).grid(row=2, column=2, padx = 10)


root.mainloop()

#currently pass b/c not to run on itfs own
if__name__=='__main__'
pass
