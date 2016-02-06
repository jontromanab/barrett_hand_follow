#!/usr/bin/env python



import rospy, actionlib
import thread


from sensor_msgs.msg import JointState
from control_msgs.msg import FollowJointTrajectoryAction
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint



class BarrettHandTrajectoryFollower:
    """ This controller controls the barrett hand in Gazebo with a follow_joint_trajectory action server. Though the spread joints are fixed.TODO """
    def __init__(self):
        rospy.init_node('bhand_controller')
        rospy.loginfo('Gripper controller Started'  ) 

        
        

        # publisher
        self.pub = rospy.Publisher('bhand_node/command', JointState,queue_size=10)
        

        
	self.server = actionlib.SimpleActionServer("~follow_joint_trajectory", FollowJointTrajectoryAction, execute_cb=self.actionCb, auto_start=False)
        
        self.server.start()
        rospy.spin()

    def actionCb(self, goal):
        
        rospy.loginfo('Gripper controller action goal recieved  with %d waypoints '  %len(goal.trajectory.points)) 
        rospy.loginfo('The spread joints are fixed'  ) 
        
	msg = JointState()
    	
	#rospy.loginfo('Joints are %s'  %goal.trajectory.joint_names[1]) 
	for i in range(0,len(goal.trajectory.points)):
		msg = JointState()
		msg.name = goal.trajectory.joint_names
		msg.header.stamp = rospy.Time.now()
    		msg.header.frame_id = ''
		msg.position=goal.trajectory.points[i].positions
		#rospy.loginfo('j12 values are %s'  %goal.trajectory.points[i].positions[1])
        	self.pub.publish(msg)
        
        #rospy.sleep(5.0)
        self.server.set_succeeded()
        rospy.loginfo('Gripper Controller: Done.')

if __name__=='__main__': 
    try:
        BarrettHandTrajectoryFollower()
    except rospy.ROSInterruptException:
        rospy.loginfo('Done!!!!!!')
        

