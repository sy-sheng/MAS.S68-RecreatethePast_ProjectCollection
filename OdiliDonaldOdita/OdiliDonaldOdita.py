import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np

def triangle(A,B,C,color):
    coordinate=[
        (A[0],A[1]), #top
        (B[0],B[1]), #left
        (C[0],C[1]), #right
        (A[0],A[1])#ignored
    ]

    boundrys=[
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
    ]
    paths = Path(coordinate, boundrys)
    patch = patches.PathPatch(paths, edgecolor=color, facecolor=color, linewidth=2.5)
    return patch

def rectangle(A,B,C,D,color):
    coordinate=[
        (A[0],A[1]), #topleft
        (B[0],B[1]), #topright
        (C[0],C[1]), #bottomright
        (D[0],D[1]), #bottomleft
        (A[0],A[1])#ignored
    ]

    boundrys=[
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
    ]
    paths = Path(coordinate, boundrys)
    patch = patches.PathPatch(paths, edgecolor=color, facecolor=color, linewidth=0)
    return patch

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

colorlist=["#B74D6E","#D3434D","#FFC834","#B66350","#EC9826","#538BD8","#2C3352","#8D9ECB"]
colorlist2=["#177DD0","#2B90E1","#4FA78D","#A7C948","#EECF00","#4CBA4D","#F29138"]
colorlist3=["#3B5282","#51A68B","#FFC834","#E39432","#FB9E46","#2180AB","#4E85D1","#CD4A51"]



for i in range(1000):
    ax.cla()
    ax.set_facecolor(np.random.choice(colorlist))

    for i in range(41):
        i=i+1
        x1=np.random.randint(-50,50)
        d1=np.random.normal(10,15)
        A1=(x1,50)
        B1=(x1+d1,50)
        C1=((x1+d1/2),-70)
        ax.add_patch(triangle(A1,B1,C1,np.random.choice(colorlist)))

    for i in range(41):
        i=i+1
        x1=np.random.randint(-50,50)
        d1=np.random.normal(10,15)
        A1=(x1,-70)
        B1=(x1+d1,-70)
        C1=((x1+d1/2),50)
        ax.add_patch(triangle(A1,B1,C1,np.random.choice(colorlist)))

    k1=-80
    k2=-80
    j=0

    for i in range(50):
        if(k1>0 or k2>0):
            break
        else:        
            A2=(0,0)
            B2=(k1,-k1)
            C2=(k2,k2)
            c=colorlist2[j]
            ax.add_patch(triangle(A2,B2,C2,c))
            k1=k1+np.random.randint(-10,15)
            k2=k2+np.random.randint(-10,15)
            if(j<(len(colorlist2)-1)):
                j=j+1
            else:
                j=0

    x31=80
    x32=-80
    j1=0

    for i in range(50):
        if(x31<0 or x32>0):
            break
        else:
            A2=(0,0)
            B2=(x31,x31)
            C2=(x32,-x32)
            c=colorlist3[j1]
            ax.add_patch(triangle(A2,B2,C2,c))       
            x31=x31-np.random.randint(-10,15)
            x32=x32+np.random.randint(-10,15)
            if(j1<(len(colorlist3)-1)):
                j1=j1+1
            else:
                j1=0
    ax.set_xlim(-50, 50)
    ax.set_ylim(-70, 50)

    #turn off xy-axis
    frame = plt.gca()
    frame.axes.get_yaxis().set_visible(False)
    frame.axes.get_xaxis().set_visible(False)
    plt.pause(0.1)

plt.show()
