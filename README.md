# Research-Track-1-Assignment-1
This Respotiory is for Reseach Track assignment 1
## 👨‍💻 Author
Name: Nimai Dey
University: University of Genova

Course: Robotics Engineering - Research Track 1


# 🐢 Research Track 1 - Assignment 1

Welcome to my **ROS-based project** developed as part of the _Research Track 1_ course.  
This project uses the **Turtlesim simulator** and demonstrates basic ROS concepts including node communication, topics, publishing, and subscribing.

---

## 📦 Project Structure

```bash
assignment1_rt/
├── launch/
│   └── assignment1.launch
├── scripts/
│   ├── ui_node.py
│   ├── control_turtle_node.py
│   └── distance_node.py
├── CMakeLists.txt
├── package.xml
└── README.md
## 📦 Features
Move turtles in the Turtlesim environment using keyboard input

Monitor distance between turtle1 and turtle2

Automatically stop turtles if they get too close or near boundaries

Simple and clean ROS node communication
## 🛠️ How to Run
# 1 Source your workspace:
source ~/catkin_ws/devel/setup.bash
# 2 Launch the full system:
roslaunch assignment1_rt assignment1.launch
# 3 Use the keyboard input in the terminal to control the turtle.
## 📂 Nodes Description
ui_node.py
Captures user input (e.g., w, a, s, d) and publishes movement commands.

control_turtle_node.py
Subscribes to user commands and controls turtle motion accordingly.

distance_node.py
Calculates and publishes the distance between turtle1 and turtle2.
Stops movement if they get too close or if the turtle approaches the window boundaries.

 ## 📚 Dependencies
ros-noetic

turtlesim

Python 3
## 💡 Future Improvements
Add GUI-based controls

Use RViz for visualization

Implement collision detection with more turtles

##-----See you soon-----






