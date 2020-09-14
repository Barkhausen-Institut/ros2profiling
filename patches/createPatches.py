#!/usr/bin/env python

"""This script goes through all changes that were made in some ROS2
source directories, and creates a patch for them in the present
directiory.

"""

import subprocess
import pathlib

def check_call(cmd):
    print (cmd)
    subprocess.check_call(cmd, shell=True)

def check_output(cmd):
    print(cmd)
    return subprocess.check_output(cmd, shell=True).decode('utf-8')

def processDirectory(f):
    thisDir = pathlib.Path(__file__).resolve().parent
    cd = f"cd {thisDir}/../../{f}"
    base = pathlib.PurePath(f).name
    bi_url = f"https://github.com/Barkhausen-Institut/{base}.git"
    destination = f"{thisDir}"

    # 1. format-patch to somewhere
    check_call(f"{cd} && git add . && git diff HEAD > {destination}/{base}.patch")
    
def main():
    folders = ["ros2/demos",
               "ros2/common_interfaces", 
               "ros2/rcl",
               "ros2/rclcpp",
               "ros2/rmw_connext",
               "ros2/rmw_cyclonedds",
               "ros2/rmw_fastrtps",
]

    for f in folders:
        print(f"=== {f} ===============================")
        processDirectory(f)
        print("==================================")

    

if __name__ == '__main__':
    main()
