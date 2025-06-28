import os , sys
from os.path import dirname, join , abspath

parent_dir_path =  abspath(join(dirname(__file__),".."))
sys.path.insert(0,parent_dir_path)

from student import student_details

def teacher():
    print("This is teacher details")

student_details.student()


#__pycache__ also known as pyc file : These are compiled python files(source code to byte code, stored in .pyc file inside __pycache__ directory)
# This helps in speedup loading the module next time it is imported
