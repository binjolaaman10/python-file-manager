'''
This is a python based file manager system
for microsoft windows made by Aman Binjola
as a personal project.
28-November-2019
'''

# ! python3

import sys
import os
import shutil
# import send2trash

print('Welcome to Zolo File Manager\n')

# Stores every drive connected on PC in a list.
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]

while True:
    print("1.Open files/folders \n2.Rename \n3.Move and Paste \n4.Copy and Paste \n5.Delete\n")
    result = input("Choose one of the following: ")

    if result == '1':
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
                break

            elif inp == '2':
                path = 'C:\\Users\\$USERNAME\\Videos'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '3':
                path = 'C:\\Users\\$USERNAME\\Pictures'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '4':
                path = 'C:\\Users\\$USERNAME\\Downloads'
                os.chdir(os.path.expandvars(path))
                break

            elif inp in drives:
                os.chdir(inp + '\\')
                break

            else:
                print('Error\nEnter a correct input / drive name.\n')

        while True:

            listdir = os.listdir(os.getcwd())
            for x in os.listdir(os.getcwd()):
                print(x)

            print('\n\nType "exitManager" to exit from file manager.')
            print('Type "backManager" to go up one directory.')
            res = input('\nChoose a file/folder: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    os.system(res)
                else:
                    os.chdir(res)
                    for x in os.listdir(os.getcwd()):
                        print(x)

            elif res == 'exitManager':                                             # Exit command to exit from loop
                sys.exit(1)

            elif res == 'backManager':                                             # Back command to go up one directory
                os.chdir('..')

            else:
                print('No file exist of this name.')

    if result == '5':
        while True:

            # Options to delete files/folders to permanently or otherwise
            print('\n\n1. Permanently \n2. Recycle Bin')
            query = input('Would you like to permanently delete or send to Recycle Bin?: ')

            if query == '1':
                print('You chose to permanently delete files/folders.')
                # code

            elif query == '2':
                print('You chose to temporarily delete files/folders.')
                # code

            else:
                print('You chose wrong number')
