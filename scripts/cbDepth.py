#!usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
import csv
import numpy as np

def msg2CV(msg):
    bridge = CvBridge()
    try:
        image = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        return image
    except CvBridgeError as e:
        print(e)
        return

def cbDepth(msg):
    print("callback!")
    image = msg2CV(msg)
    cv2.imshow('raw image', image)
    cv2.circle(image,(0,0),15,(255,0,0),-1)
    cv2.waitKey(1)
    file_path='/home/anny/realSense/catkin_ws/src/depth_app/scripts/'
    np.save(file_path + 'tree_turn', image)
    with open(file_path + 'output_turn.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(image)
    


if __name__ == "__main__":
    rospy.init_node("depthHandler", anonymous=True)
    subDepth = rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", Image, cbDepth)
    print("successfully initialized!")
    rospy.spin()
