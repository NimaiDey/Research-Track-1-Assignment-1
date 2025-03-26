cmake_minimum_required(VERSION 3.0.2)
project(assignment1_rt)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  turtlesim
)

## Declare catkin package
catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs turtlesim
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Install Python scripts
catkin_install_python(PROGRAMS
  scripts/ui_node.py
  scripts/control_turtle_node.py
  scripts/distance_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)