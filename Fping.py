# To create a GUI
from tkinter import *
# To create a Table
from tkinter import ttk
# To work with Shell Commands
import os

# Function to Clear the Text Area
def ClearTxtArea():
    TxtArea.delete(1.0, END)

# Function to Clear the Table
def Cleartable():
    global IID

    for record in table.get_children():
        table.delete(record)

    IID = 0

# Function to Clear Selected Records in the Table
def ClearTableSelectedFping():
    for record in table.selection():
        table.delete(record)

# Function to run the Shell Command
def PerformFping():
    global IID

    # Writing to the Fping Data Input File from Text Area
    file = open(FpingInputFile, "w")
    file.write(TxtArea.get(1.0, END))
    file.close()

    # Running the Shell Command
    command="fping < "+FpingInputFile+" > "+FpingOutputFile+" 2>&1"
    os.system(command)

    # Opening the Fping Data Output File
    file = open(FpingOutputFile, "r")
    # Filling the Actual Data in the Table
    for line in file:
        record = line.split(" ")
        # If service is alive or unreachable, then add service name and the status
        if record[2] == "alive\n" or record[2] == "unreachable\n":
            table.insert(parent='', index='end', iid=IID, values=([record[0], record[2].upper()]))
        # If service cannot be identified, then add service name and UNKNOWN NAME/SERVICE status
        else:
            table.insert(parent='', index='end', iid=IID, values=([record[0][:len(record[0])-1], "UNKNOWN NAME/SERVICE"]))
        IID += 1

# Input Data file for Fping
FpingInputFile = "FpingInputData.txt"
# Output Data file for Fping
FpingOutputFile = "FpingOutputData.txt"
# IID is used to insert rows into the table
IID = 0

# Creating the Main Window
MainWindow = Tk()
# Adding Title to the Main Window
MainWindow.title("Fping Command")

# Creating a Frame for the Table
frame = Frame(MainWindow)
# Creating a Scrollbar for the Frame
scroll = Scrollbar(frame)
# Creating the Actual Table
table = ttk.Treeview(frame, yscrollcommand=scroll.set)
# Configuring the Scrollbar for the Table
scroll.config(command=table.yview)

# Headings for Columns of Fping
tableHeadings = ["IP Address / Host Name", "Status"]
# Width for Columns of Fping
tableWidth = [200, 200]

# Initializing Table Columns
table['columns'] = tableHeadings
# Formatting Table Columns
table.column("#0", width=0, stretch=NO)
for index in range(len(tableHeadings)):
    table.column(tableHeadings[index], anchor=E, width=tableWidth[index])
# Setting the Headings Text of Table Columns
table.heading("#0", text="#0")
for index in range(len(tableHeadings)):
    table.heading(tableHeadings[index], text=tableHeadings[index])

# Creating a Text Area field to input Addresses
TxtArea = Text(MainWindow, width=40, height=5)
# Creating a Button frame to place all Buttons
BtnFrame = Frame(MainWindow)

# Creating a Button to Clear the Table
CleartableButton = Button(BtnFrame, text="Clear Fping Table", command=Cleartable)
# Creating a Button to Clear Selected Records in the Table
ClearTableSelectedFpingButton = Button(BtnFrame, text="Remove Selected Entries", command=ClearTableSelectedFping)
# Creating a Button to Clear the Text Area
ClearTxtAreaButton = Button(BtnFrame, text="Clear Text", command=ClearTxtArea)
# Creating a Button to Perform Fping Operation
PerformFpingButton = Button(BtnFrame, text="Perform Fping on given data!", command=PerformFping)

# Adding Components to the Main Window
frame.pack(pady=10)
scroll.pack(side=RIGHT, fill=Y)
table.pack()
TxtArea.pack(pady=10)
BtnFrame.pack()

# Adding Components to the Button Frame
CleartableButton.grid(row=0, column=0)
ClearTableSelectedFpingButton.grid(row=0, column=1)
ClearTxtAreaButton.grid(row=1, column=0)
PerformFpingButton.grid(row=1, column=1)

# Looping the Main Window
MainWindow.mainloop()