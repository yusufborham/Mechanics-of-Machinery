from visual import *
from math import *
from time import sleep

z = 20 
boundary = box(pos=vector(0, 0, 0), size=vector(350, 350, 0.1), color=color.white)
r2 = 20
r3 = 60 

OA = cylinder(pos=vector(0, 0, z),radius=2,axis=vector(50, 0, z),color=color.blue,round=true,shaftwidth = 5)
AB = cylinder(pos=vector(50, 0, z),radius=2,axis=vector(100, 0, z),round = true,color=color.blue,shaftwidth = 5)
piston1 = cylinder(pos=(0,0,z),radius=2,axis=(1,0,0),length=15,color=color.blue)
piston2 = cylinder(pos=(0,0,z),radius=5,axis=(1,0,0),length=4,color=color.red)

j0 = sphere(pos=vector(0, 0, z), radius=4, color=color.cyan)
j1 = sphere(pos=vector(0, 0, z), radius=4, color=color.cyan)
j3 = sphere(pos=vector(0, 0, z), radius=4, color=color.cyan)
angle = 0.0
Xa = 0
Ya = 0
Xb = 0
Yb = 0
fs = 0.01
    
while True:
    while angle < 2*3.14:
        # calculate all co-ordinates 
        Xa = r2*cos(angle)
        Ya = r2*sin(angle)
        Xb = Xa + sqrt( pow(r3,2) - pow(Ya,2))
        Yb = 0
        
        # update position for all links
        OA.axis = vector(Xa,Ya,0)
        AB.pos = vector(Xa,Ya,z)
        AB.axis = vector(Xb-Xa,Yb-Ya,0)
        
        # update positions for joints and piston 
        piston1.pos = vector(Xb,Yb,z)
        piston2.pos = vector(Xb+15,Yb,z)
        j1.pos = vector(Xa,Ya,z)
        j3.pos =  vector(Xb,Yb,z)
        
        # Set the rate 
        rate(300)
        
        # increment the angle 
        angle = angle + fs
        
    angle = 0.0
