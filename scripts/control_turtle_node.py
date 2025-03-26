#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def control_turtle():
    rospy.init_node('control_turtle_node')
    
    turtle_name = rospy.get_param('~turtle_name', 'turtle1')
    pub = rospy.Publisher(f'/{turtle_name}/cmd_vel', Twist, queue_size=10)
    
    rate = rospy.Rate(10)  # 10Hz
    twist = Twist()

    linear_speed = rospy.get_param('~linear_speed', 1.0)
    angular_speed = rospy.get_param('~angular_speed', 1.0)

    twist.linear.x = linear_speed
    twist.angular.z = angular_speed

    # Send the command for 1 second
    rospy.loginfo(f"Controlling {turtle_name} with linear speed {linear_speed} and angular speed {angular_speed} for 1 second")
    
    for _ in range(10):  # 10 iterations for 1 second
        pub.publish(twist)
        rate.sleep()

    # Stop the turtle
    twist.linear.x = 0
    twist.angular.z = 0
    pub.publish(twist)

if __name__ == '__main__':
    try:
        control_turtle()
    except rospy.ROSInterruptException:
        pass
