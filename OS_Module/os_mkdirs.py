import os

directory = "My Recursively Directory"
parent_dir = "/home/pablo/Programming/Python"
path = os.path.join(parent_dir,directory)
os.makedirs(path)
print("Directory '%s' created" %directory )

directory = "c"
parent_dir = "/home/pablo/Programming/Python/a/b"
mode = 0o777
path = os.path.join(parent_dir,directory)
os.makedirs(path,mode)
print("Directory '%s' created" %directory )