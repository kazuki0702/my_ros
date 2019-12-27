#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def cb(message):
    print('{0}yard = {1}m'.format(message.data,message.data/1.0936))

if __name__ == '__main__':
    rospy.init_node('sub_yard')
    sub = rospy.Subscriber('/yard', Int32, cb)
    rospy.spin()
"""
import rospy
from std_msgs.msg import Int32

def cb(message):
    print('{0}yard = {1}m'.format(message.data,message.data/1.0936))

if __name__ == '__main__':
    rospy.init_node('sub_yard')
    sub = rospy.Subscriber('/yard', Int32, cb)
    rospy.spin()
"""
