#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def rotate():
    #Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Converting from angles to radians
    angular_speed = 0.2

    #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    spin_time = (PI/2)/angular_speed
    
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    while(rospy.Time.now().to_sec()-100 < t0):
        t = rospy.Time.now().to_sec()

        while(rospy.Time.now().to_sec()-10 < t):
            vel_msg.linear.x=0.2
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
        
        t = rospy.Time.now().to_sec()
        
        while(rospy.Time.now().to_sec()-spin_time < t):
            vel_msg.linear.x = 0
            vel_msg.angular.z = angular_speed
            velocity_publisher.publish(vel_msg)


    #Forcing our robot to stop
    vel_msg.angular.z = 0
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()

if __name__ == '__main__':
    try:
        # Testing our function
        rotate()
    except rospy.ROSInterruptException:
        pass