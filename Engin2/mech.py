from machines import *

addJoint(Point(100,0,0))
addJoint(Point(0,0,0))
addJoint(Point(0,0,0))

addLink(joints[0].startPos,Point(100,0,0))
addLink(joints[1].startPos , Point(50,50,0))
addLink(joints[2].startPos,Point(0,0,0))
r2 = 20
r3 = 50
while True:
    while angle < 2*3.14:
        # calculate all co-ordinates 
        Xa = r2*cos(angle)
        Ya = r2*sin(angle)
        Xb = Xa + sqrt( pow(r3,2) - pow(Ya,2))
        Yb = 0
        #
        updateLinkPos(1,joints[0].startPos , Point(Xa,Ya,0))
        updateLinkPos(2,joints[1].startPos , Point(Xb,Yb,0))
        updateLinkPos(3,joints[2].startPos , Point(Xb + 10,Yb,0))
        
        # Set the rate 
        rate(300)
        
        # increment the angle 
        angle = angle + 0.01
        
    angle = 0.0