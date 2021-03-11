import os

# Remove Files
file_todel = input("Insert the file name: ")
path_file = "/home/pablo/Programming/Python/ToDelete"
path = os.path.join(path_file,file_todel)
os.remove(path)

#Remove Directory
path_dir = "/home/pablo/Programming/Python/ToDelete"
directory = "MyDir2"

path = os.path.join(path_dir,directory)
os.rmdir(path)