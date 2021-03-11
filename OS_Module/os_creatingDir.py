import os

#Directory name
directory = "OS_Module"

# #Parent directory path
parent_dir = "/home/pablo/Programming/Python"

# #path
path = os.path.join(parent_dir,directory)

#Create the directory
os.mkdir(path)
print("Directory '%s' created" %directory)



#Another Directory
directory = "GeeksForGeeks"
parent_dir = "/home/pablo/Programming/Python"
mode = 0o666
path = os.path.join(parent_dir,directory)
os.mkdir(path,mode)
print("Directory '%s' created" %directory)

#Another
path = os.path.join("/home/pablo/Programming/Python","MyDirectory")
os.mkdir(path,0o666)
print("Directory created")