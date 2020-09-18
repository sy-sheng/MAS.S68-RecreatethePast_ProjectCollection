from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colorlist=["#E4007F", "#FFF100", "#0099D9", "#5A595F"]

a1=[]
a2=[]
a3=[]
size=[]
color=[]
beta=[]
theta=0
a=30

for l in range(30):
    theta=theta+(np.pi/15)
    l=l+1
    for k in range(60):
        h=np.random.normal(0, 40)        
        s=np.random.normal(10, 20)/(np.abs(h)*0.1+1)  
        a1.append(a*np.cos(theta))
        a2.append(a*np.sin(theta))
        a3.append(h)
        size.append(s)
        facecolor=np.random.choice(colorlist)
        color.append(facecolor)
        k=k+1 

th=0
number=len(a1)
th=np.pi/360
r=0

for i in range(720):
    
    ax.cla()    
    ax.scatter(a1, a2, a3, s=size, c=color, alpha=0.8)

    for r in range(number):  
        a1[r]=a*np.cos(np.arccos(a1[r]/a)+th)
        a2[r]=a*np.sin(np.arcsin(a2[r]/a)+th)
        r=r+1
   
    i=i+1

    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    ax.set_zlim(-50, 50)
    plt.axis('off')
    plt.pause(0.1)

plt.show()