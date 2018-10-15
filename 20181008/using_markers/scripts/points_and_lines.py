#!/usr/bin/env python
#coding=utf-8
import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
import math
import time

def talker():
    #Publisher 函数第一个参数是话题名称，第二个参数 数据类型，现在就是我们定义的msg 最后一个是缓冲区的大小
    #queue_size: None（不建议）  #这将设置为阻塞式同步收发模式！
    #queue_size: 0（不建议）#这将设置为无限缓冲区模式，很危险！
    #queue_size: 10 or more  #一般情况下，设为10 。queue_size太大了会导致数据延迟不同步。
    pub = rospy.Publisher('visualization_marker', Marker , queue_size=10)
    rospy.init_node('points_and_lines', anonymous=True)
    #更新频率是30hz
    rate = rospy.Rate(30) 

    f = 0.0

    while not rospy.is_shutdown():
	    points = line_strip = line_list = Marker()

	    points.header.frame_id = "/my_frame"
	    line_strip.header.frame_id = "/my_frame"
	    line_list.header.frame_id = "/my_frame"

	    points.header.stamp = rospy.Time.now()
	    line_strip.header.stamp = rospy.Time.now()
	    line_list.header.stamp = rospy.Time.now()

	    points.ns = "points_and_lines"
	    line_strip.ns = "points_and_lines"
	    line_list.ns = "points_and_lines"

	    points.action = Marker.ADD
	    line_strip.action = Marker.ADD
	    line_list.action = Marker.ADD

	    points.pose.orientation.w = 1.0
	    line_strip.pose.orientation.w = 1.0
	    line_list.pose.orientation.w = 1.0

	    points.id = 0
	    line_strip.id = 1
	    line_list.id = 2

	    points.type = Marker.POINTS
	    line_strip.type = Marker.LINE_STRIP
	    line_list.type = Marker.LINE_LIST

	    points.scale.x = 0.2
	    points.scale.y = 0.2

	    line_strip.scale.x = 0.1
	    line_list.scale.x = 0.1

	    # Points are green
	    points.color.r = 0.0
	    points.color.g = 1.0
	    points.color.b = 0.0
	    points.color.a = 1.0

	    # Line strip is blue
	    line_strip.color.r = 0.0
	    line_strip.color.g = 0.0
	    line_strip.color.b = 1.0
	    line_strip.color.a = 1.0

	    # Line list is red
	    line_list.color.r = 1.0
	    line_list.color.g = 0.0
	    line_list.color.b = 0.0
	    line_list.color.a = 1.0

	    # Create the vertices for the points and lines
	    for i in xrange(100):
	    	y = 5*math.sin(f+i/100.0*2*math.pi)
	    	z = 5*math.cos(f+i/100.0*2*math.pi)
	    	p = Point()
	    	p.x = i-50
	    	p.y = y
	    	p.z = z

	    	points.points.append(p)
	    	line_strip.points.append(p)
	    	# The line list needs two points for each line
	    	# line_list.points.append(p)
	    	# p.z =  z + 1.0
	    	# line_list.points.append(p)

	    pub.publish(points)
	    pub.publish(line_strip)
	    # pub.publish(line_list)

	    rate.sleep()
	    # f = f + 0.04

if __name__ == '__main__':
    talker()

