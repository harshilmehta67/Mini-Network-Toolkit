# To create a GUI
from tkinter import *
# To create a Table
from tkinter import ttk
# To work with Shell Commands
import os

# Function to Clear the Traceroute Table
def Cleartable():
    for record in table.get_children():
        table.delete(record)

# Function to Perform Traceroute
def PerformTroute():
    # Clear the Table
    Cleartable()

    # Run Shell Command
    command="traceroute "+address.get()+" | awk '{ if(NR > 1) printf \"%s|%s|%s|%s|%s|%s\\n\", $1, $2, $3, $4, $6, $8 }' > "+TracerouteOutputFile
    os.system(command)

    # Opening the Traceroute Data File
    file = open(TracerouteOutputFile, "r")
    # Filling the Actual Data in the Table
    IID=0
    for line in file:
        record = line.split("|")
        table.insert(parent='', index='end', iid=IID, values=record)
        IID += 1

# Data File for Traceroute Table
TracerouteOutputFile = "TracerouteOutputData.txt"

# Creating the Main Window
MainWindow = Tk()
# Adding Title to the Main Window
MainWindow.title("Traceroute Command")

# Creating a Frame for the Table
frame = Frame(MainWindow)
# Creating a Scrollbar for the Frame
scroll = Scrollbar(frame)
# Creating the Actual Table
table = ttk.Treeview(frame, yscrollcommand=scroll.set)
# Configuring the Scrollbar for the Table
scroll.config(command=table.yview)

# Headings for Columns of Traceroute
TracerouteTableHeadings = ["Hop", "Name", "IP Address", "RTT 1", "RTT 2", "RTT 3"]
# Width for Columns of Traceroute
TracerouteTableWidth = [100, 300, 200, 100, 100, 100]

# Initializing Table Columns
table['columns'] = TracerouteTableHeadings
# Formatting Table Columns
table.column("#0", width=0, stretch=NO)
for index in range(len(TracerouteTableHeadings)):
    table.column(TracerouteTableHeadings[index], anchor=E, width=TracerouteTableWidth[index])
# Setting the Headings Text of Table Columns
table.heading("#0", text="#0")
for index in range(len(TracerouteTableHeadings)):
    table.heading(TracerouteTableHeadings[index], text=TracerouteTableHeadings[index])

# Creating a label
label = Label(MainWindow, text="Enter the Address you want to trace route to below:")
# Creating a (Form) entry
address = Entry(MainWindow, width=40)
# Creating a button to Trace the Route taken by Packet
traceButton = Button(MainWindow, text="Trace the Route!", command=PerformTroute)

# Adding the components to the Main Window
frame.pack(pady=20)
scroll.pack(side=RIGHT, fill=Y)
table.pack()
label.pack()
address.pack()
traceButton.pack(pady=30)

# Looping the Main Window
MainWindow.mainloop()