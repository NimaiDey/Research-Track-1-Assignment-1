#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

def spawn_turtle():
    rospy.wait_for_service('/spawn')
    try:
        spawn = rospy.ServiceProxy('/spawn', Spawn)
        # Spawn turtle2 at (2, 2) with heading 0
        spawn(2, 2, 0, "turtle2")
        rospy.loginfo("Turtle2 spawned successfully.")
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

def control_turtle(turtle_name, linear_speed, angular_speed):
    pub = rospy.Publisher(f'/{turtle_name}/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    twist = Twist()
    twist.linear.x = linear_speed
    twist.angular.z = angular_speed

    # Send the command for 1 second
    for _ in range(10):  # 10 iterations to run for 1 second
        pub.publish(twist)
        rate.sleep()

    # Stop the turtle after 1 second
    twist.linear.x = 0
    twist.angular.z = 0
    pub.publish(twist)

def ui_node():
    rospy.init_node('ui_node')
    
    # Spawn turtle2 if it hasn't been spawned yet
    spawn_turtle()

    while not rospy.is_shutdown():
        turtle_name = input("Which turtle would you like to control? (turtle1 or turtle2): ")
        try:
            linear_speed = float(input("Enter linear speed: "))
            angular_speed = float(input("Enter angular speed: "))
        except ValueError:
            rospy.logwarn("Invalid input. Please enter numeric values for speed.")
            continue

        control_turtle(turtle_name, linear_speed, angular_speed)
        rospy.loginfo(f"Sent command to {turtle_name} for 1 second.")

if __name__ == '__main__':
    try:
        ui_node()
    except rospy.ROSInterruptException:
        pass
