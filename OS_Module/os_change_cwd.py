import os

def get_current():
    print("Current Working Directory: ",os.getcwd())

get_current()

os.chdir('/home/pablo/Courses')
get_current()

