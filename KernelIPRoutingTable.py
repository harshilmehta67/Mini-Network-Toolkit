# To create a GUI
from tkinter import *
# To create a Table
from tkinter import ttk
# To work with Shell Commands
import os

# Headings for Columns of Kernel IP Routing Table
KernelIPRoutingTableHeadings = ["Destination", "Gateway", "Genmask", "Flags", "MSS", "Window", "irtt", "Interface"]
# Width for Columns of Kernel IP Routing Table
KernelIPRoutingTableWidth = [200, 150, 180, 75, 75, 75, 75, 100]
# Data File for Kernel IP Routing Table
KernelIPRoutingFile = "KernelIPRoutingData.txt"

# Creating the Main Window
MainWindow = Tk()
# Adding Title to the Main Window
MainWindow.title("Kernel IP Routing Table")

# Creating a Frame for the Table
frame = Frame(MainWindow)
# Creating a Scrollbar for the Frame
scroll = Scrollbar(frame)
# Creating the Actual Table
table = ttk.Treeview(frame, yscrollcommand=scroll.set)
# Configuring the Scrollbar for the Table
scroll.config(command=table.yview)

# Initializing Table Columns
table['columns'] = KernelIPRoutingTableHeadings
# Formatting Table Columns
table.column("#0", width=0, stretch=NO)
for index in range(len(KernelIPRoutingTableHeadings)):
    table.column(KernelIPRoutingTableHeadings[index], anchor=W, width=KernelIPRoutingTableWidth[index])
# Setting the Headings Text of Table Columns
table.heading("#0", text="#0")
for index in range(len(KernelIPRoutingTableHeadings)):
    table.heading(KernelIPRoutingTableHeadings[index], text=KernelIPRoutingTableHeadings[index])

# Running the Shell Command
command="netstat -r | awk \'{ if(NR > 2) printf \"%s|%s|%s|%s|%s|%s|%s|%s\\n\", $1, $2, $3, $4, $5, $6, $7, $8 }\' > "+KernelIPRoutingFile
os.system(command)

# Opening the Kernel Interface Data File
file = open(KernelIPRoutingFile, "r")
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