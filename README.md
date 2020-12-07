#### Our project is a mini network management toolkit which allows its users to perform some network related functions and monitoring activity. The point of such a toolkit is to ease the pain of managing the network administrators so that they would not need large and complex softwares just to perform some basic housekeeping.
- Some features of our toolkit are:
  - Fetching the system information.
  - Fetching the Interface Table and the Routing table of the machine.
  - Viewing the connections made by internet sockets and/or unix sockets
  - Capturing and viewing ICMP, TCP and UDP packets
  - Testing whether an IP address or a set of IP addresses are active or unreachable
  - Tracing the path taken by a packet during its journey to the provided machine
  
1. Start by updating the package list using the following command:

  ``` sudo apt update ```

2. Now, to run this project you'll need a python version 3+. Then to download pip you need to run

  ``` sudo apt install python3-pip```

3. Firstly, to install all the dependencies, you need to have a version of python pip(python3:pip3 used here)

  ``` pip3 install -r requirements.txt ```

4. Also to properly link the _python-tkinter_, run this
  ``` sudo apt-get install python3-tk ```

5. After installing all the dependencies, the main file is [MiniNetworkToolkit.py](https://github.com/harshilmehta67/Mini-Network-Toolkit/blob/main/MiniNetworkToolkit.py).To run this file, 

  ``` sudo python3 MiniNetworkToolkit.py ``` 

## The project is up and running with a nice GUI!
