#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
import math

# Distance threshold and boundary limits
DIST_THRESHOLD = 1.0  # Stop if turtles are within 1.0 units
X_MIN, X_MAX = 1.0, 10.0
Y_MIN, Y_MAX = 1.0, 10.0

class DistanceMonitor:
    def __init__(self):
        rospy.init_node("distance_node", anonymous=True)

        self.pose1 = None
        self.pose2 = None

        self.dist_pub = rospy.Publisher("/turtle_distance", Float32, queue_size=10)
        self.vel_pub = rospy.Publisher("/turtle2/cmd_vel", Twist, queue_size=10)

        rospy.Subscriber("/turtle1/pose", Pose, self.callback_turtle1)
        rospy.Subscriber("/turtle2/pose", Pose, self.callback_turtle2)

        rospy.loginfo("Distance monitoring node started.")
        rospy.spin()

    def callback_turtle1(self, data):
        self.pose1 = data
        self.check_distance()

    def callback_turtle2(self, data):
        self.pose2 = data
        self.check_distance()

    def check_distance(self):
        if self.pose1 is None or self.pose2 is None:
            return

        # Compute Euclidean distance
        dist = math.sqrt((self.pose1.x - self.pose2.x)**2 + (self.pose1.y - self.pose2.y)**2)
        self.dist_pub.publish(dist)
        rospy.loginfo(f"Distance between turtles: {dist:.2f}")

        # Check distance threshold
        if dist < DIST_THRESHOLD:
            rospy.logwarn("Turtles too close! Stopping movement.")
            self.stop_turtle()

        # Check boundary limits
        if not (X_MIN <= self.pose2.x <= X_MAX and Y_MIN <= self.pose2.y <= Y_MAX):
            rospy.logwarn("Turtle2 near boundary! Stopping movement.")
            self.stop_turtle()

    def stop_turtle(self):
        stop_msg = Twist()
        self.vel_pub.publish(stop_msg)  # Send zero velocity

if __name__ == "__main__":
    try:
        DistanceMonitor()
    except rospy.ROSInterruptException:
        pass
