#!/usr/bin/env python
#coding=utf-8
import rospy
from visualization_msgs.msg import Marker

def talker():
    #Publisher 函数第一个参数是话题名称，第二个参数 数据类型，现在就是我们定义的msg 最后一个是缓冲区的大小
    #queue_size: None（不建议）  #这将设置为阻塞式同步收发模式！
    #queue_size: 0（不建议）#这将设置为无限缓冲区模式，很危险！
    #queue_size: 10 or more  #一般情况下，设为10 。queue_size太大了会导致数据延迟不同步。
    pub = rospy.Publisher('visualization_marker', Marker , queue_size=10)
    rospy.init_node('basic_shapes', anonymous=True)
    #更新频率是1hz
    rate = rospy.Rate(1) 
    
    marker = Marker()

    # Set the frame ID and timestamp.  See the TF tutorials for information on these.
    marker.header.frame_id = "/my_frame"
    marker.header.stamp = rospy.Time.now()

    # Set the namespace and id for this marker.  This serves to create a unique ID
    # Any marker sent with the same namespace and id will overwrite the old one
    marker.ns = "basic_shapes"
    marker.id = 0

    # Set the marker type.  Initially this is CUBE, and cycles between that and SPHERE, ARROW, and CYLINDER
    marker.type = Marker.CUBE

    # Set the marker action.  Options are ADD, DELETE, and new in ROS Indigo: 3 (DELETEALL)
    marker.action = Marker.ADD

    #Set the pose of the marker.  This is a full 6DOF pose relative to the frame/time specified in the header
    marker.pose.position.x = 0
    marker.pose.position.y = 0
    marker.pose.position.z = 0
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0

    # Set the scale of the marker -- 1x1x1 here means 1m on a side
    marker.scale.x = 1.0
    marker.scale.y = 1.0
    marker.scale.z = 1.0

    # Set the color -- be sure to set alpha to something non-zero!
    marker.color.r = 0.0
    marker.color.g = 1.0
    marker.color.b = 0.0
    marker.color.a = 1.0

    marker.lifetime = rospy.Duration()

    while not rospy.is_shutdown():
        pub.publish(marker)

        if marker.type == Marker.CUBE:
        	marker.type = Marker.SPHERE
        elif marker.type == Marker.SPHERE:
        	marker.type = Marker.ARROW
        elif marker.type == Marker.ARROW:
        	marker.type = Marker.CYLINDER
       	elif marker.type == Marker.CYLINDER:
       		marker.type = Marker.CUBE

        rate.sleep()


if __name__ == '__main__':
    talker()
 

