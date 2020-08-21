# ROS2 Profiling

A package to provide functions for intra-layer profiling.  This packages is used in the Publication ...

It currently is targeting the [Foxy-20200807](https://github.com/ros2/ros2/blob/release-foxy-20200807/ros2.repos) ROS2 Release, but may work for later projects as well.

Technically, the repository contains several patch files which are applied to the official ROS2 sources. Use the script `patches/applyPatches.py` to apply them. Once you have made changes to the official sources, do not commit them there, but run `patches/createPatches.py` to collect all changes in patch files within this repository.
