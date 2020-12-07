# To create a GUI
from tkinter import *
# To create a Table
from tkinter import ttk
# To work with Shell Commands
import os

# Headings for Columns of Packet Information Table
ConnectionDetailsTableHeadings = ["State", "Recv-Q", "Send-Q", "Local Address:Port", "Foreign Address:Port"]
# Width for Columns of Packet Information Table
ConnectionDetailsTableWidth = [90, 70, 70, 150, 450]
# Data File for Packet Information Table
ConnectionDetailsFileName = "ConnectionDetails.txt"
# List of Packet CheckBoxes Selected
PacketCheckButtonsSelected = []

# Creating the Main Window
MainWindow = Tk()
# Adding Title to the Main Window
MainWindow.title("Packet Information")

# Creating a Frame for the Table
frame = Frame(MainWindow)
# Creating a Scrollbar for the Frame
scroll = Scrollbar(frame)
# Creating the Actual Table
table = ttk.Treeview(frame, yscrollcommand=scroll.set)
# Configuring the Scrollbar for the Table
scroll.config(command=table.yview)

# Function to Clear the whole table
def ClearTable():
    for record in table.get_children():
        table.delete(record)

# Function to get selected checkboxes
def GetSelectedPackets():
    # Assigning no. of Packets selected to 0
    NumberOfPacketsSelected = 0
    # Initializing the Selected Options to NULL
    SelectedOptions = ""
    # Traverse through the list of Checkboxes
    for index in range(len(PacketCheckButtonsSelected)):
        # If a particular Checkbox is checked
        if PacketCheckButtonsSelected[index].get() >= 1:
            # Increment the no. of Packets Selected
            NumberOfPacketsSelected += 1
            # Append the checked option to Selected Options
            SelectedOptions += ","+str(Packets[index])
    # Return the string as well as the no. of Packets selected
    return [NumberOfPacketsSelected, SelectedOptions[1:]]

# Function to Run the Shell Command
def RunCommand():
    # Getting the no. of Packets and Packets List
    [NumberOfPackets, PacketsList] = GetSelectedPackets()
    # If no. of Packets is zero
    if NumberOfPackets == 0:
        # Do nothing and terminate
        return
    
    # Running the Shell Command
    Command = "ss -r -A '"+PacketsList+"' | awk \'{ if(NR > 1) printf \"%s|%s|%s|%s|%s|%s\\n\", $1, $2, $3, $4, $5, $6 }\' > "+ConnectionDetailsFileName
    os.system(Command)

    # If no. of Packets is more than 1 or if 'inet' or 'unix' is selected, then one more column is required
    if NumberOfPackets != 1 or PacketCheckButtonsSelected[0].get() == 1 or PacketCheckButtonsSelected[4].get() == 1:
        # Add one more column to the Column Headings
        ConnectionDetailsTableHeadings = ["Protocol", "State", "Recv-Q", "Send-Q", "Local Address:Port", "Foreign Address:Port"]
        # Add the width of the same column to Column Widths
        ConnectionDetailsTableWidth = [90, 90, 70, 70, 150, 450]
    else:
        # Keep the same 5 Column Headings
        ConnectionDetailsTableHeadings = ["State", "Recv-Q", "Send-Q", "Local Address:Port", "Foreign Address:Port"]
        # Keep the same 5 Column Widths
        ConnectionDetailsTableWidth = [90, 70, 70, 150, 450]

    # Clear the Table to get rid of Previous Data
    ClearTable()
    
    # Initializing Table Columns
    table['columns'] = ConnectionDetailsTableHeadings
    # Formatting Table Columns
    table.column("#0", width=0, stretch=NO)
    for index in range(len(ConnectionDetailsTableHeadings)):
        table.column(ConnectionDetailsTableHeadings[index], anchor=E, width=ConnectionDetailsTableWidth[index])
    # Setting the Headings Text of Table Columns
    table.heading("#0", text="#0")
    for index in range(len(ConnectionDetailsTableHeadings)):
        table.heading(ConnectionDetailsTableHeadings[index], text=ConnectionDetailsTableHeadings[index])

    # Opening the Packet Information Data File
    file = open(ConnectionDetailsFileName, "r")
    # Filling the Actual Data in the Table
    count = 0
    for line in file:
        record = line.split("|")
        table.insert(parent='', index='end', iid=count, values=(record))
        count += 1

# Making a list of all possible packets    
Packets = [
    "inet",
    "tcp",
    "udp",  
    "raw",  
    "unix",  
    "packet",  
    "netlink",  
    "unix_dgram",  
    "unix_stream",  
    "unix_seqpacket",
    "packet_raw", 
    "packet_dgram",  
    "dccp", 
    "sctp", 
    "vsock_stream", 
    "vsock_dgram",
    "xdp"
]

# Adding Components to the Main WIndow
frame.pack(pady=20)
scroll.pack(side=RIGHT, fill=Y)
table.pack()

# Creating a new Frame to hold Components
ComponentsFrame = LabelFrame(MainWindow, text="Select Packets")
# Adding this Frame to the Main Window
ComponentsFrame.pack(padx=20, pady=20)
# Making and Adding Checkboxes to the Main Window
PacketCheckButtons = []
for index in range((len(Packets))):
    option = IntVar()
    # Initializing the Checkbox to zero
    option.set(0)
    PacketCheckButtonsSelected.append(option)
    # Adding the Checkboxes to the list
    PacketCheckButtons.append(Checkbutton(ComponentsFrame, text=Packets[index], variable=PacketCheckButtonsSelected[index]))
    # Adding the Components to the Frame
    PacketCheckButtons[index].grid(row=index%2, column=int(index/2), padx=5, pady=5)
    
# Making the Submit Button
SubmitButton = Button(ComponentsFrame, text="Submit", command=RunCommand)
# Making the Clear Table Button
ClearButton = Button(ComponentsFrame, text="Clear Table", command=ClearTable)
# Adding the Clear Table Button to the Main Window
ClearButton.grid(row=4, column=1, padx=30, pady=30)
# Adding the SUbmit Button to the Main WIndow
SubmitButton.grid(row=4, column=7, padx=30, pady=30)

# Looping the Main Window
MainWindow.mainloop()