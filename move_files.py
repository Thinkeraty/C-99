import os
import shutil

source = input("Enter the source path :")
destination = input("Enter the destination path: ")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)

for list in list_of_files:
    shutil.move((source + list), destination)