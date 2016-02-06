#!/usr/bin/env python
import rospy
from std_msgs.msg import *
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import *

#individual publishers for the joints
pub_bhand=rospy.Publisher("/bhand_node/command",JointState, queue_size=10)



def callback(data):
    
    
    traj_ = JointTrajectory()
    msg = JointState()
    rate = rospy.Rate(10) # 10hz
    
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.joint_names)	
    msg.header=data.header;
    msg.name=data.joint_names;
    
    msg.position=data.points[0].positions
    msg.velocity=data.points[0].velocities 
    msg.effort=data.points[0].effort 
    pub_bhand.publish(msg);
    
    #msg.name = []
    #msg.position = []
    #msg.velocity = []
    #msg.effort = []
       
    #for i in range(0,7):
       # msg.name.append(data.name[i])   
        #msg.position.append(data.position[i]) 
        #msg.velocity.append(data.velocity[i])
        #msg.effort.append(data.effort[i])            
    
    #msg.header.stamp = rospy.Time.now()
    #msg.header.frame_id = ''
    #joint_states_pub.publish(msg)  
	
       


	

def listener():
     
#Initialize the bhand node
    rospy.init_node('hand_controller', anonymous=False)
#Creating the topic for subscribing commands
    rospy.Subscriber('%s/command'%rospy.get_name(), JointTrajectory, callback)
#Creating the service for performing different grasp mode.Always try to start from Initialization mode: rosservice call /bhand_node/actions 1
    
    
    rospy.spin()


    



if __name__ == '__main__':
    listener()
    
