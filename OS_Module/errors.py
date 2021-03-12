import os

#Print OS name
print(os.name)

#OS error in the case of invalid or inaccesible file names and paths

try:
    #If the file not exist, get a IOError
    filename = 'delete_directories.py'
    f = open(filename,'rU')
    text = f.read()
    print(text)
    f.close()
except IOError:
    print(f"Problem reading: {filename} ")
