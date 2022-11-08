
import sys
import psutil
import platform

if len(sys.argv) == 1:
    
    print("Please enter an argument. For example, -d for distro -m for memory, -c for CPU, -u for user info, -l for load average, -i for IP address.")
    sys.exit()

if len(sys.argv) > 2:

    print("Please enter only one argument. For example, -d for distro -m for memory, -c for CPU, -u for user info, -l for load average, -i for IP address.")
    sys.exit()
    
if sys.argv[1] not in ["-d", "-m", "-c", "-u", "-l", "-i"]:
    
    print("Please enter a valid argument. For example, -d for distro -m for memory, -c for CPU, -u for user info, -l for load average, -i for IP address.")
    sys.exit()
    
if sys.argv[1] == "-d":
    
    import platform
    print(platform.uname())
    
if sys.argv[1] == "-m":
    
    import psutil
    print(psutil.virtual_memory())
    
if sys.argv[1] == "-c":
    
    import psutil
    print(psutil.cpu_times())
    
if sys.argv[1] == "-u":
    
    import getpass
    print(getpass.getuser())
    
if sys.argv[1] == "-l":
    
    import os
    print(os.getloadavg())
    
if sys.argv[1] == "-i":
    
    import socket
    print(socket.gethostbyname(socket.gethostname()))
    
