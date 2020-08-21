#!/usr/bin/env python

"""This script applies the patches named <pkg>.patch to <pkg>, where <pkg> is defined in the main function

Invoke with `python applyPatches.py` from the `patches` directory of the ros2 profiling directory
""".

import subprocess
import pathlib

def check_call(cmd):
    print (cmd)
    subprocess.check_call(cmd, shell=True)

def check_output(cmd):
    print(cmd)
    return subprocess.check_output(cmd, shell=True).decode('utf-8')

def processDirectory(f):
    authors = """--author="Maximilian*" --author="orola*" --author="mmatthe" """
    thisDir = pathlib.Path(__file__).resolve().parent
    cd = f"cd {thisDir}/../../{f}"
    base = pathlib.PurePath(f).name
    bi_url = f"https://github.com/Barkhausen-Institut/{base}.git"
    destination = f"{thisDir}"

    # 1. reset
    check_call(f"{cd} && git reset --hard")

    # 2. apply
    patch = f"{destination}/{base}.patch"
    check_call(f"{cd} && git apply --reject --whitespace=fix {patch}")

   
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
