#!/usr/bin/env python3
from swirlypy.swirlytool import *
import argparse
import os
from courses import import_course_path

print("Welcome to swirlpy! What can I call you? \n")

user_name = input("Please enter your name: \n")

print("Thanks", user_name + "!", "Lets cover some basic commands in swirlpy\n")

print("Whenever you see '...', that means you should press Enter when you are ready. \n")

print("... <- your cue to press Enter to continue \n")

input("")

print("Below are the available courses you can choose from: \n")

path = str(import_course_path.get_path())

# print(filter(os.path.isdir, os.listdir(path)))
print(next(os.walk( os.path.join(path,'.')))[1])


course_select = input("Select a course: \n")

print("Choose from the following commands: ('run', 'info', 'create', 'test')")

command = input("Enter a command for the course: \n")

main(parse([command, os.path.join(path,course_select)]))