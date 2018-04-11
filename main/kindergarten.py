import argh
import os


def find(path, name):
    "Finds folder of file if exists in given path"
    return findFirst(os.path.expanduser("~"), name)


def findFirst(path, name):
    for root, dirs, files in os.walk(path):
        print(dirs)
        if name in files:
            return os.path.join(root, name)
    else:
        return "File not found"


parser = argh.ArghParser()
parser.add_commands([findFirst])


if __name__ == '__main__':
    parser.dispatch()