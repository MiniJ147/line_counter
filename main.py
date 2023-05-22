import os

#inital data
blacklist = []
blacklist_dir = []
types = []

#checking if the file is in our blacklisted files
def check_black_list(path):
        for i in range(len(blacklist)):
            if path==blacklist[i]:
                  return False
        
        return True

 #parsing the file types to push into the list
def parse_type(file):
     for i in range(len(file)-1,0,-1):
          if(file[i]=='.'):
               return file[i:len(file)]

#parsing the specfic data out of the strings to push to the list
def parse_user_input_str(str):
    lower = 0
    data = []
    
    for i in range(len(str)):
        if(str[i]==','):
            data.append(str[lower:i])
            lower=i+1
    data.append(str[lower:len(str)])
    return data

#checking if dir is banned
def is_dir_banned(path):
    #must = '' because if user enters nothing then it returns a blank str
    if(blacklist_dir[0]==''):
        return False
    
    for i in range(len(blacklist_dir)):
         if blacklist_dir[i]==path:
              return True
    return False

def Directory(dir_path):
    total_lines = 0
    files = []
    sub_dir = []

    #grabbing data
    for path in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            if(check_black_list(path)):
                #must = '' because if user enters nothing then it returns a blank str
                if(types[0]==''):
                    files.append(path)
                else:
                    for i in range(len(types)):
                         if types[i]==parse_type(path):
                              files.append(path)  
                              break        
        else:
            if not(is_dir_banned(path)):
                sub_dir.append(path)

    print("Sub Dir: "+str(sub_dir))

    #recursively searching through the sub directorys of the project
    for i in range(len(sub_dir)):
          total_lines+=Directory(dir_path+'\\'+sub_dir[i])

    #counting lines
    for i in range(len(files)):
        with open(r""+dir_path+"\\"+files[i], 'r') as fp:
            num_lines = sum(1 for line in fp)
            total_lines += num_lines
            print('('+files[i]+') Total lines:', num_lines)

    return total_lines

#grabbing user input
dir_path = input("Enter Project Path\n>>> ")
blacklist_str = input("\nEnter blacklist files (put a , to seperate)\n>>> ")
types_str = input("\nEnter specfic file types to count (put a , to seperate) (EX: main.c --> \'.c\')\n>>> ")
blacklist_dir_str = input("\nEnter excluded directory (put a , to seperate)\n>>> ")

#parsing data and pushing it into the list
blacklist = parse_user_input_str(blacklist_str)
blacklist_dir = parse_user_input_str(blacklist_dir_str)
types = parse_user_input_str(types_str)

#printing data
print("\nSpecfic: "+str(types))
print("Blacklist: "+str(blacklist))
print("Blacklist Dir: "+str(blacklist_dir))
print("\nProjects Total Lines: "+str(Directory(dir_path)))

input(">>>") 