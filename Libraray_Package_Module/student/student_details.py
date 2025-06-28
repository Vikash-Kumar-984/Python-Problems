# Why the need of creating different scripts for students and teachers?
# To maintain the code, to improve understanding of the code

# Best Practice: To keep different components in different scripts
# e.g., model training and EDA should be kept in different scripts

# Modules: A module is a single file (with .py extension) that contains the python code
# Inside module function, class or variables or some python code
# e.g., student_details.py and teacher_details.py are modules

# Package: It is a collection of modules organised in directories
# Each directory can have multiple python scripts
# e.g., student and teacher folder is packages

# Version before python 3.3, to make a package it was necessary to include __init__.py in package (to initialise package and expose required modules and functions)

# Library: It is the collection of multiple package and modules
#         : pre-written code to perform common task
#         e.g., pandas, numpy

# Importing teacher_details module from teacher package

# from teacher import teacher_details #from is used with package, import is used with modules (generic)
import os, sys
# os provides functionality to interact with operating system
# sys provides access to system specific parameters and function such as python path

# Output: The path to script:  /workspaces/Python-Problems/Libraray_Package_Module/student/student_details.py

from os.path import dirname, join, abspath

# Dirname: will give the directory containing the current script

# Join: join two or more paths, inserting '/' as needed

# print("The directory to script: ",abspath(join(dirname(__file__),"..")))
# The directory to script:  /workspaces/Python-Problems/Libraray_Package_Module/student
# Output: The path to script:  /workspaces/Python-Problems/Libraray_Package_Module/student/student_details.py

# The join(dirname(__file__),"..")) directory to script:  /workspaces/Python-Problems/Libraray_Package_Module/student/..
# The abspath(join(dirname(__file__),"..")) directory to script:  /workspaces/Python-Problems/Libraray_Package_Module
# abspath(join(dirname(__file__),"..")): abspath converts the relative path to absolute path

parent_dir_path =  abspath(join(dirname(__file__),".."))
sys.path.insert(0,parent_dir_path)
# At index 0, add this directory to the beginning of module search / system path
# It allows to search modules and packages

# from teacher import teacher_details
def student():
    print("This is student details")

# teacher_details.teacher()