#!/usr/bin/env python
#coding=utf-8
import rospy
#导入mgs到pkg中
from sensor_msgs.msg import LaserScan

#回调函数输入的应该是msg
def callback(scan):
    #LaserScan消息的格式
    #std_msgs/Header header
    #float32 angle_min
    #float32 angle_max
    #float32 angle_increment
    #float32 time_increment
    #float32 scan_time
    #float32 range_min
    #float32 range_max
    #float32[] ranges
    #float32[] intensities
    rospy.loginfo("\r\n\r\nstart")
    rospy.loginfo(scan.header)
    rospy.loginfo(scan.ranges)
    rospy.loginfo("end\r\n\r\n")

def listener():
    rospy.init_node('pylistener', anonymous=False)
    #Subscriber函数第一个参数是topic的名称，第二个参数是接受的数据类型 第三个参数是回调函数的名称
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

