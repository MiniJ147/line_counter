import os 
from collections import deque

total, files = 0, deque()
directories = [input("Enter Dir:\n>>> ")]
blacklist = set(list(input("Enter Blacklist Dir (name), file (name.type), or file types (.type):\n>>> ").split(" ")))
special = set(list(input("Enter Special file types to count (.go, .cpp)\nLeave Blank if you don't want to be specfic\n>>> ").split(" ")))

#weird glitch
if '' in blacklist: blacklist.remove('')
if '' in special: special.remove('')

special_active = len(special) > 0

print("CURR SETTINGS:\nBlacklist: ",blacklist,"\nSpecial Active: ",special_active," ",special)

while directories:
    current_dir = directories.pop()
    scan = os.scandir(current_dir)
    for entry in scan:
        name = entry.path.split("\\")[-1]
        if entry.is_dir() and not name in blacklist: directories.append(entry.path)
        elif entry.is_file() and not name in blacklist:
            file_type = "."+name.split(".")[-1]
            if special_active and file_type in special: files.append(entry.path)
            elif not special_active and not file_type in blacklist: files.append(entry.path)
    scan.close()

while files:
    curr = files.popleft()
    lines = len(open(curr,'r').readlines())
    print(curr.split("\\")[-1],lines)
    total+=lines

print("Total: ",total)