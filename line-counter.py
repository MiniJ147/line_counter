import os 
import sys
from collections import deque

#gathering input
total, files = 0, deque()
directories = deque([input("Enter Dir:\n>>> ")]) if len(sys.argv) == 1 else deque([sys.argv[1]])
blacklist = set(input("Enter Blacklist Dir (name), file (name.type), or file types (.type):\n>>> ").split(" "))
special = set(input("Enter Special file types to count (.go, .cpp)\nLeave Blank if you don't want to be specfic\n>>> ").split(" "))

#weird glitch where '' are inputed
if '' in blacklist: blacklist.remove('')
if '' in special: special.remove('')

special_active = len(special) > 0
print("\nCURR SETTINGS:\nBlacklist: ",blacklist,"\nSpecial Active: ",special_active," ",special,end="\n\n")

#BFS search on source file directory
while directories: #loop until out of directories
    current_dir = directories.popleft() 
    scan = os.scandir(current_dir) #gather files and directories
    for entry in scan: #loop over scan
        name = entry.path.split("\\")[-1] #grab file/directory name
        if entry.is_dir() and not name in blacklist: directories.append(entry.path) #add if not blacklist and is directory
        elif entry.is_file() and not name in blacklist: #if it's a file and not blacklisted
            file_type = "."+name.split(".")[-1] #get file type
            if special_active and file_type in special: files.append(entry.path) #add if we are checking special and its special
            elif not special_active and not file_type in blacklist: files.append(entry.path) #if not special and not blacklisted
    scan.close() #close current scan and keep looping

#count files queued up through search
while files:
    curr = files.popleft()
    lines = len(open(curr,'r',encoding="utf8").readlines()) # count 
    print(curr.split("\\")[-1],lines) #print file then line count
    total+=lines

print("Total: ",total)