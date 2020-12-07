# To create a GUI
from tkinter import *
# To create a Table
from tkinter import ttk
# To work with Shell Commands
import os

# Headings for Columns of Kernel Interface Table
KernelInterfaceTableHeadings = ["Interface", "MTU", "RX-OK", "RX-ERR", "RX-DRP", "RX-OVR", "TX-OK", "TX-ERR", "TX-DRP", "TX-OVR", "Flg"]
# Width for Columns of Kernel Interface Table
KernelInterfaceTableWidth = [90, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]
# Data File for Kernel Interface Table
KernelInterfaceFile = "KernelInterfaceData.txt"

# Creating the Main Window
MainWindow = Tk()
# Adding Title to the Main Window
MainWindow.title("Kernel Interface Table")

# Creating a Frame for the Table
frame = Frame(MainWindow)
# Creating a Scrollbar for the Frame
scroll = Scrollbar(frame)
# Creating the Actual Table
table = ttk.Treeview(frame, yscrollcommand=scroll.set)
# Configuring the Scrollbar for the Table
scroll.config(command=table.yview)

# Initializing Table Columns
table['columns'] = KernelInterfaceTableHeadings
# Formatting Table Columns
table.column("#0", width=0, stretch=NO)
for index in range(len(KernelInterfaceTableHeadings)):
    table.column(KernelInterfaceTableHeadings[index], anchor=E, width=KernelInterfaceTableWidth[index])
# Setting the Headings Text of Table Columns
table.heading("#0", text="#0")
for index in range(len(KernelInterfaceTableHeadings)):
    table.heading(KernelInterfaceTableHeadings[index], text=KernelInterfaceTableHeadings[index])

# Running the Shell Command
command="netstat -i | awk \'{ if(NR > 2) printf \"%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|\\n\", $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11 }\' > "+KernelInterfaceFile
os.system(command)

# Opening the Kernel Interface Data File
file = open(KernelInterfaceFile, "r")
# Filling the Actual Data in the Table
count = 0
for line in file:
    record = line.split("|")
    table.insert(parent='', index='end', iid=count, values=record)
    count += 1

# Adding the Components to the Main Window
frame.pack(padx=20, pady=20)
scroll.pack(side=RIGHT, fill=Y)
table.pack()

# Looping the Main Window
MainWindow.mainloop()