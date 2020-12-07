# To create a GUI
from tkinter import *
# To work with Shell Commands
import os

# Function to Open System Details Window
def OpenSystemDetails():
    os.system("python3 SystemDetails.py")

# Function to Open Kernel Interface Table Window
def OpenKernelInterfaceTable():
    os.system("python3 KernelInterfaceTable.py")

# Function to Open Kernel IP Routing Table Window
def OpenKernelIPRoutingTable():
    os.system("python3 KernelIPRoutingTable.py")

# Function to Open Packet Information Window
def OpenConnectionDetails():
    os.system("python3 ConnectionDetails.py")

# Function to Open Fping Window
def OpenFping():
    os.system("python3 Fping.py")

# Function to Open Traceroute Window
def OpenTraceroute():
    os.system("python3 Traceroute.py")

# Function to Open Packet Sniffer Window
def OpenPacketSniffer():
    os.system("sudo python3 PacketSniffer.py")

# Creating the Main Window
MainWindow = Tk()
# Adding Title to the Main Window
MainWindow.title("Mini Network Toolkit")

# Creating Buttons to Open Windows
Button1 = Button(MainWindow, text="View Client System Details", width = 25, command=OpenSystemDetails)
Button2 = Button(MainWindow, text="View (Kernel) Interface Table", width = 25, command=OpenKernelInterfaceTable)
Button3 = Button(MainWindow, text="View (Kernel) IP Routing Table", width = 25, command=OpenKernelIPRoutingTable)
Button4 = Button(MainWindow, text="View Connection Details", width = 25, command=OpenConnectionDetails)
Button5 = Button(MainWindow, text="Open Fping Console", width = 25, command=OpenFping)
Button6 = Button(MainWindow, text="Open Traceroute Console", width = 25, command=OpenTraceroute)
Button7 = Button(MainWindow, text="Sniff Packets", width = 25, command=OpenPacketSniffer)

# Adding Buttons to Main Window
Button1.pack(padx=10, pady=10)
Button2.pack(padx=10, pady=10)
Button3.pack(padx=10, pady=10)
Button4.pack(padx=10, pady=10)
Button5.pack(padx=10, pady=10)
Button6.pack(padx=10, pady=10)
Button7.pack(padx=10, pady=10)

# Looping the Main Window
MainWindow.mainloop()
