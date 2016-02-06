#!/usr/bin/env python



import rospy, actionlib
import thread

from control_msgs.msg import GripperCommandAction
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
from math import asin

class ParallelGripperActionController:
    """ A simple controller that operates two opposing servos to
        open/close to a particular size opening. """
    def __init__(self):
        rospy.init_node('bhand_controller')
        

        
        

        # publishers
        self.pub = rospy.Publisher('bhand_node/command', JointState,queue_size=10)
        

        # subscribe to command and then spin
        self.server = actionlib.SimpleActionServer('~gripper_action', GripperCommandAction, execute_cb=self.actionCb, auto_start=False)
        self.server.start()
        rospy.spin()

    def actionCb(self, goal):
        
        rospy.loginfo('Gripper controller action goal recieved:%f' % goal.command.position)
        command = goal.command.position
        
        # publish msgs
        
	msg = JointState()
    	msg.name = []
    	
	
        msg.position.append(goal.command.position) 
        #msg.velocity.append(data.velocity[i])
        msg.effort.append(goal.command.max_effort)            
    
    	msg.header.stamp = rospy.Time.now()
    	msg.header.frame_id = ''
    
        self.pub.publish(msg)
        
        rospy.sleep(5.0)
        self.server.set_succeeded()
        rospy.loginfo('Gripper Controller: Done.')

if __name__=='__main__': 
    try:
        ParallelGripperActionController()
    except rospy.ROSInterruptException:
        rospy.loginfo('Hasta la Vista...')
        

