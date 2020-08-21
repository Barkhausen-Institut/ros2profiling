#!/usr/bin/env python

"""Do not use this script!

This script was used to create patches from the forked ROS2 repos onto a tagged version of ROS.
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
    authors = """--author="Maximilian*" --author="orola*" --author="mmatthe" """
    thisDir = pathlib.Path(__file__).resolve().parent
    cd = f"cd {thisDir}/../../{f}"
    base = pathlib.PurePath(f).name
    bi_url = f"https://github.com/Barkhausen-Institut/{base}.git"
    destination = f"{thisDir}"

    # 0. reset hard
    check_call(f"{cd} && git reset --hard")
    check_call(f"{cd} && git cherry-pick --abort || true")

    # 1. add remote
    check_call(f"{cd} && git remote rm bi || true")
    check_call(f"{cd} && git remote add bi {bi_url} || true")

    # 2. fetch
    check_call(f"{cd} && git fetch bi master")

    # 3. find commits
    commits = check_output(f"{cd} && git log --reverse --pretty=format:\"%H\" --no-merges {authors} bi/master")
    num = len(commits.split())
    commits = " ".join(commits.split())
    

    # 6. cherry-pick
    print (f"Cherry-picking {num} commits:")
    print ("\n".join(commits.split()))
    check_call(f"{cd} && git cherry-pick -n {commits}")

    # 6. format-patch to somewhere
    check_call(f"{cd} && git diff HEAD > {destination}/{base}.patch")
    
def main():
    folders = ["ros2/demos",
               "ros2/common_interfaces",
               "ros2/rcl",
               "ros2/rclcpp",
               "ros2/rmw_connext",
               "ros2/rmw_cyclonedds"
#               "ros2/rmw_fastrtps",
]

    for f in folders:
        print(f"=== {f} ===============================")
        processDirectory(f)
        print("==================================")

    

if __name__ == '__main__':
    main()
