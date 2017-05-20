"""Importing os to access file system"""
import os

PATH = "/data/users/" #path to folder with insufficient rights for listing
DICC = "/var/tmp/common.txt" #path to folders dictionary from dirb

def attempt_path(path):
    """Check if file or directory exists and print out the result. Return true if directory"""

    if os.path.isfile(path):
        print "Found file : " + path
        return False

    if os.path.isdir(path):
        print "Found dir  : " + path
        return True

    return False

def look_for_subdirs(path):
    """Recursive function to look for dirs"""
    with open(DICC) as dicc:
        for line in dicc:
            curr_path = path + line.rstrip('\n')
            if attempt_path(curr_path):
                look_for_subdirs(curr_path + "/")

look_for_subdirs(PATH)
print "Finished"
