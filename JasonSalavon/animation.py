import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import PIL
from PIL import Image
from skimage import io

def average_color(path):
    img=io.imread(path)
    # img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)  
    average=img.mean(axis=0).mean(axis=0)
    b=average[0]/255
    g=average[1]/255
    r=average[2]/255
    r=round(r,2)
    g=round(g,2)
    b=round(b,2)
    color=(r,g,b)
    return color

colorlist=[]
for i in range(9231):
    k=i+1
    path='img/'+str(k)+'.jpg'
    color=average_color(path)
    colorlist.append(color)

num=1000
fig, ax = plt.subplots(figsize=(25,6))
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
plt.xticks([])
plt.yticks([])
n=len(colorlist)

for i in range(1000000):
    ax.cla()    
    w=1
    num=2000

    # n=len(colorlist)
    for j in range (num):
        x=(w*j+i)%num
        ax.add_patch(
            patches.Rectangle(
                (x,0),
                w,
                100,
                color=colorlist[j]
            )
        )
    #settings for the canvas
    plt.xlim(0,num)
    plt.ylim(0,100)
    plt.axis('off')

    # Note that using time.sleep does *not* work here!
    plt.pause(0.01)

plt.show()