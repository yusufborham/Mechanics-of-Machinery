from visual import *
from math import *
boundary = box(pos=vector(0, 0, 0), size=vector(350, 350, 0.1), color=color.white)
class Point :
    def __init__(self,x,y,z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    def __str__(self):
        print(str(self.x),str(self.y),str(self.z))
class Mechanism :
    def __init__(self,startPos,endPos):
        self.startPos = startPos 
        self.endPos = endPos
class Joint(Mechanism) :
    def __init__(self,startPos):
        Mechanism.__init__(self,startPos,endPos=Point(0,0,0))
        self.joint = sphere(pos=vector(startPos.x, startPos.y, startPos.z), radius=4, color=color.cyan)
    def update(self,newPos):
        self.startPos = newPos
        self.joint.pos = vector(self.startPos.x, self.startPos.y, self.startPos.z)
class Link(Mechanism) :
    def __init__(self,startPos,endPos):
        # link it with the link before
        Mechanism.__init__(self,startPos,endPos)
        # set a starting point and an ending point
        #build the linkage and the end joint
        self.linkage = cylinder(pos=vector(startPos.x,startPos.y,startPos.z ),radius=2,axis=vector(endPos.x,endPos.y ,endPos.z ),color=color.blue,round=true,shaftwidth = 5)
    def updatePos(self,newStartPos,newEndPos):
        self.startPos = newStartPos
        self.endPos = newEndPos
        # change linkage start position 
        self.linkage.pos = vector(newStartPos.x,newStartPos.y,newStartPos.z)
        # change linkage end position 
        self.linkage.axis =vector(newEndPos.x , newEndPos.y ,newEndPos.z)
joints = [Joint(Point(0,0,0))]
links = []
co_ordinates = [Point(0,0,0)]

def subPoints(point1 , point2):
    return ( Point(point1.x - point2.x , point1.y - point2.y , point1.z - point2.z) )
def addJoint(point):
    joints.append(Joint(point))

def addLink(point,point2):
    links.append(Link(point,point2))

def updateLinkPos(linkNumber,point1 , point2):
    if linkNumber == 1 :
        links[linkNumber - 1].updatePos(point1 , point2)
    else :
        links[linkNumber - 1].updatePos(point1 , subPoints(point2,joints[linkNumber - 1].startPos))
        
    joints[linkNumber].update(point2)
        

# l1.updatePos(newEndPos = Point(45,45,0))
# l2.updatePos(newStartPos = Point(45,45,0) ,newEndPos=(100,30,0))
