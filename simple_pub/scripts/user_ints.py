#!/usr/bin/env python 
# license removed for brevity 

import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter', String , queue_size=10)
    rospy.init_node('talker', anonymous=True) 
    
    
    num = str(input("Input any number: "))
    teller = "You wrote the number {} {}".format(num, "\n")
        
    rospy.loginfo(teller)
    pub.publish(num)



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass