#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:10:30 2020

@author: yueshan
"""

import rospy
from duckietown.dtros import DTROS, NodeType
from sensor_msgs.msg import CompressedImage, Image
from duckietown_msgs.msg import WheelsCmdStamped
import gym_duckietown
from gym_duckietown.simulator import Simulator
from cv_bridge import CvBridge
import cv2

def init():
    env = Simulator(
        seed=123, # random seed
        map_name="loop_empty",
        max_steps=500001, # we don't want the gym to reset itself
        domain_rand=0,
        camera_width=640,
        camera_height=480,
        accept_start_angle_deg=4, # start close to straight
        full_transparency=True,
        distortion=True,
    )   
    return env
    
class ROSWrapper(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(ROSWrapper, self).__init__(node_name=node_name, node_type=NodeType.GENERIC)
        self.bridge = CvBridge()

        self.pub = rospy.Publisher('/fakebot/camera_node/image/compressed', CompressedImage, queue_size=1)
        self.sub = rospy.Subscriber('/fakebot/wheels_driver_node/wheels_cmd', WheelsCmdStamped, self.callback)
        self.action=[0.1,0.1]
        
    def imagepublisher(self,observation):
        #rate = rospy.Rate(5)
        b,g,r=cv2.split(observation)
        img=cv2.merge([r,g,b])
        #img_msg=self.bridge.cv2_to_compressed_imgmsg(observation)
        img_msg=self.bridge.cv2_to_compressed_imgmsg(img)
        img_msg.header.stamp=rospy.Time.now()
        #rospy.loginfo("Get an image...")
        self.pub.publish(img_msg)
        #rospy.loginfo("Published to topic camera_node/image/compressed")
        #rate.sleep()    
            
    def callback(self,wheelcommand):
        rospy.loginfo("get wheel command")
        self.action=[wheelcommand.vel_left,wheelcommand.vel_right]
        

if __name__ == '__main__':
    #initialize simulator
    env=init()
    
    # create the node
    node = ROSWrapper(node_name='simulatorwrapper')
    rate = rospy.Rate(50)
    #start simulation
    while True:
        
        action = node.action
        observation, reward, done, misc = env.step(action)
        node.imagepublisher(observation)
        env.render()
        if done:
            env.reset()
        rate.sleep() 

    # keep spinning
    #rospy.spin()
