from machines import *

addJoint(Point(0,0,0))
addJoint(Point(0,0,0))
addJoint(Point(0,0,0))
addJoint(Point(0,0,0))

addLink(joints[0].startPos,Point(100,0,0))
addLink(joints[1].startPos ,Point(50,50,0))
addLink(joints[2].startPos,Point(0,0,0))

r2 = 40 # length of the link 2 (side link)
r3 = 75 # length of the link 3 (coupler link)
r4 = 70 # length of the link 4 (side link)
Xq = 30 # length of fixed link (link 1)
Yq = 0

# s + l <= p + q -> Grashof's condition
# r3 + r2 <= r4 + Xq -> Grashof's condition

while True:
    while angle < 2*3.14:
        # calculate all co-ordinates 
        Xa = r2*cos(angle)
        Ya = r2*sin(angle)
        
        d = sqrt((Xq - Xa)**2 + (Yq - Ya)**2 )
        
        
        # calculate the angles
        cosD = (Xq - Xa) / d 
        sinD = (Yq - Ya) / d
        
        if cosD > 0 and sinD > 0 :
            thetaD = acos(cosD)
        elif cosD < 0 and sinD > 0 :
            thetaD = 3.14 - acos(-cosD)
        elif cosD < 0 and sinD < 0 :
            thetaD = 3.14 + acos(cosD)
        else:
            thetaD = 6.28 - acos(-cosD)
            
        theta3 = acos((d**2 + r3**2 - r4**2) / (2*d*r3)) + thetaD
        
        Xb = r3*cos(theta3) + Xa
        Yb = r3*sin(theta3) + Ya
        
        # update the position of the links
        updateLinkPos(1,joints[0].startPos , Point(Xa,Ya,0))
        updateLinkPos(2,joints[1].startPos , Point(Xb,Yb,0))
        updateLinkPos(3,Point(Xb,Yb,0),Point(Xq,Yq,0),connect = False)
        
        # Set the rate 
        rate(300)
        
        # increment the angle 
        angle = angle + 0.01
        
    angle = 0.0
