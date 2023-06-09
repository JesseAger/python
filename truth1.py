import os
from math import*
import time

'''the program gets the library and system infomation from the operating system
and prints out the current working directory'''
def current_directory():
    cwd = os.getcwd():
        print(cwd)
def file_path(name):
    path= os.path.abspath((name))
    print(path)
    current directory()
    name = "scripttest.txt"
    file_path(name)
    epc = time.time()
print(epc)
localtime = time.locatime(epc)
print(localtime)
print(time.ctime(epc))

character = "giraffe academy"
my_num = 4
numero = 2.6
print(character. replace("giraffe", "Light"))
name = (character. replace("giraffe", "Light"))
print(character.upper())
print(pow(my_num, 3))
print(ceil(numero))
print(floor(numero))
OTP= input("Enter your OneTimePassword:")
print("The " + name + " verification OTP is " + OTP)
print("Roses are {colour}")
print("{Plural} are blue")
print("I love {celebrity}")
Client = ["Jimmy", "Jayden", "Jt", "Mercy", "Frank"]
Codes = [4004, 2909, 6998, 1536, 3302]

if Client.index("Jimmy") == 0:
    # Your code here for when the first client is "Jimmy"

    print("Jimmy's code is " + Codes.index("4004"))
else:
    # Your code here for when the first client is not "Jimmy"
    print("First client is not Jimmy")


     


