# Write the python program to print the contents of a directory using the os module.
import os

# select the folder
directory_path = '/'

# using os module to get items
contents = os.listdir(directory_path)

print(contents)