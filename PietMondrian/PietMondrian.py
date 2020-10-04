import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import random

def DrawTriangle(A,B,C,D,color):
    coordinate=[
        (A[0],A[1]), #topleft
        (B[0],B[1]), #topright
        (C[0],C[1]), #bottomright
        (D[0],D[1]), #bottomleft
        (A[0],A[1]) #ignored
    ]
    boundrys=[
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
    ]
    paths = Path(coordinate, boundrys)
    patch = patches.PathPatch(paths, edgecolor=None, facecolor=color, linewidth=0)
    return patch

width=2
RedBlue=["#2B479C","#CB3A2D","#DAD9D2"]
Color=["#CB3A2D","#DAD9D2","#F3D703","#2769C0"]

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
xaxis=[]
yaxis=[]
for i in range(6):
    xaxis.append(random.randrange(0,(100-width),5))
for i in range(5):
    yaxis.append(random.randrange(width,80,5))
        
xaxis_sort=xaxis
yaxis_sort=yaxis
xaxis_sort.sort()
yaxis_sort.sort()

for i in range(1000):
    ax.cla()   
    xaxis=[]
    yaxis=[]
    for i in range(6):
        xaxis.append(random.randrange(0,(100-width),5))
    for i in range(5):
        yaxis.append(random.randrange(width,80,5))
        
    xaxis_sort=xaxis
    yaxis_sort=yaxis
    xaxis_sort.sort()
    yaxis_sort.sort()

    addA=[]
    addC=[]
    w=10

    #PATCH
    #vertical
    for i in range(4):
        k=np.random.randint(1,4)
        x1=np.random.randint(0,xaxis[-1])
        d=100
        num=0
        for j in range(6):
            x=np.abs(x1-xaxis_sort[j])
            if (x<d):
                d=x
                num=j
            else:
                continue
        x2=xaxis[num]  
        if (x1<=x2):
            x1=x1
            x2=x2
        else:
            x1temp=x1
            x1=x2
            x2=x1temp
        PointA=(x1,yaxis_sort[int(k)])
        PointB=(x2,yaxis_sort[int(k)])
        PointC=(x2,yaxis_sort[int(k-1)])
        PointD=(x1,yaxis_sort[int(k-1)])
        c=np.random.choice(Color)
        ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
        addA.append(PointA)
        addC.append(PointC)
        if (yaxis_sort[int(k)]-yaxis_sort[int(k-1)])>10:
            yi=np.random.randint(yaxis_sort[int(k-1)],yaxis_sort[int(k)],2)
            yi.sort()
            A=(x1,yi[1])
            B=(x2,yi[1])
            C=(x2,yi[0])
            D=(x1,yi[0])
            c1=np.random.choice(Color)
            ax.add_patch(DrawTriangle(A,B,C,D,c1))
            if(np.abs(yi[0]-yi[1])>5):
                a=(x1+2,yi[1]-2)
                b=(x2-2,yi[1]-2)
                c=(x2-2,yi[0]+2)
                d=(x1+2,yi[0]+2)
                c2=np.random.choice(Color)
                ax.add_patch(DrawTriangle(a,b,c,d,c2))
            else:
                continue
        else:
            continue
        i=i+1
    #horizontal
    for i in range(4):
        k=np.random.randint(1,5)
        y1=np.random.randint(0,yaxis[-1])
        d=100
        num=0
        for j in range(5):
            x=np.abs(y1-yaxis_sort[j])
            if (x<d):
                d=x
                num=j
            else:
                d=d
        y2=yaxis[num]  
        if (y1>=y2):
            y1=y1
            y2=y2
        else:
            y1temp=y1
            y1=y2
            y2=y1temp
        PointA=(xaxis_sort[int(k-1)],y1)
        PointB=(xaxis_sort[int(k)],y1)
        PointC=(xaxis_sort[int(k)],y2)
        PointD=(xaxis_sort[int(k-1)],y2)
        c=np.random.choice(Color)
        ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
        if (xaxis_sort[int(k)]-xaxis_sort[int(k-1)])>10:
            xi=np.random.randint(xaxis_sort[k-1],xaxis_sort[k],2)
            xi.sort()
            A=(xi[0],y1)
            B=(xi[1],y1)
            C=(xi[1],y2)
            D=(xi[0],y2)
            c1=np.random.choice(Color)
            ax.add_patch(DrawTriangle(A,B,C,D,c1))
            if(np.abs(xi[0]-xi[1])>5):
                a=(xi[0]+2,y1-2)
                b=(xi[1]-2,y1-2)
                c=(xi[1]-2,y2+2)
                d=(xi[0]+2,y2+2)
                c2=np.random.choice(Color)
                ax.add_patch(DrawTriangle(a,b,c,d,c2))
            else:
                continue
        else:
            continue
        i=i+1

    # #YELLOW LINES
    for i in range(5):
        PointA=(0,yaxis[i])
        PointB=(100,yaxis[i])
        PointC=(100,(yaxis[i]-width))
        PointD=(0,(yaxis[i]-width))   
        ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,"#F3D703"))

    for i in range(6):
        PointA=(xaxis[i],80)
        PointB=((xaxis[i]+width),80)
        PointC=((xaxis[i]+width),0)
        PointD=(xaxis[i],0)   
        ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,"#F3D703"))

    startpoint1=[]
    endpoint1=[]
    startpoint2=[]
    endpoint2=[]
    #RANDOM CONNECTIONS
    sub_xaxis=[]
    sub_yaxis=[]
    for i in range(5):
        sub_yaxis.append(random.randrange(width,80,5))
        sub_xaxis.append(random.randrange(0,(100-width),5))
    #xaxis
    for i in range(5):
        for j in range(6):
            while(np.abs(sub_xaxis[i]-xaxis[j])<5):
                sub_xaxis[i]=random.randrange(0,(100-width),5)
            else:
                j=j+1
        i=i+1

    #yaxis
    for i in range(5):
        for j in range(5):
            while(np.abs(sub_yaxis[i]-yaxis[j])<5):
                sub_yaxis[i]=random.randrange(width,80,5)
            else:
                j=j+1
        i=i+1
        
    for i in range(4):
        c_x=np.random.choice(xaxis,2)
        y_x=np.random.choice(sub_yaxis)
        c_x1=c_x[0]
        c_x2=c_x[1]
        if (c_x1 < c_x2):
            c_x1=c_x1
            c_x2=c_x2
        elif (c_x1 > c_x2):
            tempCx2=c_x2
            c_x2=c_x1
            c_x1=tempCx2
        else:
            pass
        PointA=(c_x1,y_x)
        PointB=(c_x2,y_x)
        PointC=(c_x2,(y_x-width))
        PointD=(c_x1,(y_x-width))
        ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,"#F3D703"))
        startpoint1.append(PointA)
        endpoint1.append(PointB)

    for i in range(4):
        c_y=np.random.choice(yaxis,2)
        x_y=np.random.choice(sub_xaxis)
        c_y1=c_y[0]
        c_y2=c_y[1]
        if (c_y1>c_y2):
            c_y1=c_y1
            c_y2=c_y2
        elif (c_y1<c_y2):
            tempCy2=c_y2
            c_y2=c_y1
            c_y1=tempCy2

        PointA=(x_y,c_y1)
        PointB=((x_y+width),c_y1)
        PointC=((x_y+width),c_y2)
        PointD=(x_y,c_y2)
        ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,"#F3D703"))    
        startpoint2.append(PointA)
        endpoint2.append(PointD)


    #SQUARES ON INTERSECTIONS

    #on the main lines
    gap=7
    for i in range(5):
        for j in range(30):
            PointA=((5+j*gap),yaxis[i])
            PointB=((5+j*gap+width),yaxis[i])
            PointC=((5+j*gap+width),(yaxis[i]-width))
            PointD=((5+j*gap),(yaxis[i]-width))
            c=np.random.choice(RedBlue)
            ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
            j=j+1
        i=i+1
    for i in range(6):
        for j in range(30):
            PointA=(xaxis[i],(5+j*gap))
            PointB=((xaxis[i]+width),(5+j*gap))
            PointC=((xaxis[i]+width),(5+j*gap-width))
            PointD=(xaxis[i],(5+j*gap-width))
            c=np.random.choice(RedBlue)
            ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
            j=j+1
        i=i+1
    #on the added lines
    #vertical
    for i in range(4):
        for j in range(20):
            x=startpoint2[i][0]
            y=startpoint2[i][1]
            end=endpoint2[i][1]
            if ((y-j*gap)>end):
                PointA=(x,(y-j*gap))
                PointB=((x+width),(y-j*gap))
                PointC=((x+width),(y-j*gap-width))
                PointD=(x,(y-j*gap-width))
                c=np.random.choice(RedBlue)
                ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
                j=j+1
            else:
                break
        i=i+1
    #horizental
    for i in range(4):
        for j in range(20):
            x=startpoint1[i][0]
            y=startpoint1[i][1]
            end=endpoint1[i][0]
            if ((x+j*gap)<end):
                PointA=((x+j*gap),y)
                PointB=((x+j*gap+width),y)
                PointC=((x+j*gap+width),(y-width))
                PointD=((x+j*gap),(y-width))
                c=np.random.choice(RedBlue)
                ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
                j=j+1
            else:
                break
        i=i+1
    #intersection of main lines
    for i in range(6):
        for j in range(5):
            PointA=(xaxis[i],yaxis[j])
            PointB=((xaxis[i]+width),yaxis[j])
            PointC=((xaxis[i]+width),(yaxis[j]-width))
            PointD=(xaxis[i],(yaxis[j]-width))
            c=np.random.choice(RedBlue)
            ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
            j=j+1
        i=i+1
    #starts and ends
    l1=len(startpoint1)
    l2=len(endpoint1)
    l3=len(startpoint2)
    l4=len(endpoint2)
    for i in range(l1):
        PointA=startpoint1[i]
        xcord=PointA[0]
        ycord=PointA[1]
        PointB=((xcord+width),ycord)
        PointC=((xcord+width),(ycord-width))
        PointD=(xcord,(ycord-width))
        c=np.random.choice(RedBlue)
        ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
    for i in range(l2):
        PointA=endpoint1[i]
        xcord=PointA[0]
        ycord=PointA[1]
        PointB=((xcord+width),ycord)
        PointC=((xcord+width),(ycord-width))
        PointD=(xcord,(ycord-width))
        c=np.random.choice(RedBlue)
        ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
    for i in range(l3):
        PointA=startpoint2[i]
        xcord=PointA[0]
        ycord=PointA[1]
        PointB=((xcord+width),ycord)
        PointC=((xcord+width),(ycord-width))
        PointD=(xcord,(ycord-width))
        c=np.random.choice(RedBlue)
        ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
    for i in range(l4):
        PointA=endpoint2[i]
        xcord=PointA[0]
        ycord=PointA[1]
        PointB=((xcord+width),ycord)
        PointC=((xcord+width),(ycord-width))
        PointD=(xcord,(ycord-width))
        c=np.random.choice(RedBlue)
        ax.add_patch(DrawTriangle(PointA,PointB,PointC,PointD,c))
    
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 80)
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    plt.pause(0.1)

plt.show()