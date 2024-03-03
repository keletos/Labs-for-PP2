import os
def listdir(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

    print("\nAll Directories and Files:")
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))

path = ""

listdir(path)

#

import os

def check_path_access(path):
    if os.path.exists(path):
        print(f"The path exists.")
    else:
        print(f"The path does not exist.")
        return
    
    if os.access(path, os.R_OK):
        print(f"The path is readable.")
    else:
        print(f"The path is not readable.")
        
    if os.access(path, os.W_OK):
        print(f"The path is writable.")
    else:
        print(f"The path is not writable.")

path = ""
check_path_access(path)

#

import os

def fpath(path):
    if os.path.exists(path):
        print(f"The path exists.")
        filename = os.path.basename(path)
        dir = os.path.dirname(path)
        print(f"Filename: {filename}")
        print(f"Directory: {dir}")
    else:
        print("The path does not exist.")

path = input()
fpath(path)

#

def countLine(f):
    c = 0
    for i in f:
        c += 1
    return c

file = open("file.txt", "r")
print(countLine(file))
file.close()

#

a = [1,2,3,4,5]

with open("file.txt", "w") as f:
    for i in a:
        f.write(str(i)+" ")

#
        
for i in range(65,91):
    name = f"{chr(i)}.txt"
    f = open(name, "w")

#

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "w")
f2.write(f1.read())
f1.close()
f2.close()

#

import os

path = ""

def isExist(path):
    if os.path.exists(path):
        os.remove(path)
        return "File deleted"
    else:
        return "File is not exists"
    
print(isExist(path))
    