'''
This is a python based file manager system
for microsoft windows made by Aman Binjola
as a personal project.
28-November-2019
'''

import os

print('Welcome to Zolo File Manager\n')

# Function to check if folders are left in the current directory.
def noFoldersLeft():
    for x in os.getcwd():
        if os.path.isdir():
            return False
    return True

# Stores every drive connected on PC in a list.
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]

# Home Screen
print('\nQuick Acess:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n')

print('Drives: ')
for x in range(len(drives)):
    print(str(5 + x) + '. ' + drives[x])

while True:
    inp = input("\nEnter your Choice: ")

    if inp == '1':
        path = 'C:\\Users\\$USERNAME\\Documents'
        os.chdir(os.path.expandvars(path))
        break;
    elif inp == '2':
        path = 'C:\\Users\\$USERNAME\\Videos'
        os.chdir(os.path.expandvars(path))
        break;
    elif inp == '3':
        path = 'C:\\Users\\$USERNAME\\Pictures'
        os.chdir(os.path.expandvars(path))
        break;
    elif inp == '4':
        path = 'C:\\Users\\$USERNAME\\Downloads'
        os.chdir(os.path.expandvars(path))
        break;
    elif inp in drives:
        os.chdir(inp + '\\')
        break;
    else:
        print('Error\nEnter a correct input.\n')


print(os.getcwd(), '\n\n')

listdir = os.listdir(os.getcwd())
for x in os.listdir(os.getcwd()):
    print(x)

res = input('\n\nChoose a file/folder: ')
print('\n')
if res in os.listdir(os.getcwd()):
    if os.path.isfile(res):
        os.system(res)
    else:
        os.chdir(res)
        for x in os.listdir(os.getcwd()):
            print(x)
else:
    print('No file exist of this name.')