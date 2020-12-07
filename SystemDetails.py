# To create a GUI
from tkinter import *
# To work with Shell Commands
import subprocess

# Function to Run Shell Commands and return their Output
def ShellCommand(command):
    # Getting the Output of Command into a String
    string = str(subprocess.check_output(command,shell=True))
    # Return that String
    return string[2:len(string)-3]

# Creating the Main Window
MainWindow = Tk()
# Adding Title to the Main Window
MainWindow.title("Client System Details")

# List of Frames
Frames = []
# List of Titles for Frames
FrameTitles = ["Kernel Name", "Node Name", "Kernel Version", "Processor Type", "Hardware Platform", "Operating System"]
# List of Command Outputs
CommandOutputs = []
# List of Commands
Commands = ["uname -s", "uname -n", "uname -v", "uname -p", "uname -i", "uname -o"]

# Creating and Adding Components to the Main Window
for index in range(len(Commands)):
    # Creating a Frame 
    frame = LabelFrame(MainWindow, text=FrameTitles[index], width=450, height=150)
    # Adding that Frame to the Frame List
    Frames.append(frame)
    # Add that Frame to the Main Window
    Frames[index].pack(padx=15, pady=15)
    # Creating a Label
    label = Label(Frames[index], text=ShellCommand(Commands[index]), width=50, height=2)
    # Adding that Label to the list of Command Outputs
    CommandOutputs.append(label)
    # Add that Command Output to the Main Window
    CommandOutputs[index].pack()

# Looping the Main Window
MainWindow.mainloop()