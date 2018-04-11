#!/usr/bin/venv python

import argh
import os


def greet(name, greeting='Hello'):
    "Greets the user with given name. The greeting is customizable."
    return greeting + ', ' + name

# def list(path):
#     print(os.listdir(os.getcwd()))
#
#
# def find(path, name):
#     "Finds folder of file if exists in given path"
#     return findFirst(os.path.expanduser("~"), name)
#
#
# def findFirst(path, name):
#     "Finds folder of file if exists in given path"
#     for root, dirs, files in os.walk(path):
#         print(dirs)
#         if name in files:
#             return os.path.join(root, name)
#     else:
#         return "File not found"


parser = argh.ArghParser()
# parser.add_commands([findFirst, list])
parser.add_commands([greet])

if __name__ == '__main__':
    parser.dispatch()
