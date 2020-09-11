import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
from matplotlib import style

#draw triangle
def triangle(c, l, color,t):  
    coordinate=[
        (c[0], c[1]-np.sqrt(3)*l/3), #bottom
        (c[0]-0.5*l, c[1]+np.sqrt(3)*l/6), #left
        (c[0]+0.5*l, c[1]+np.sqrt(3)*l/6), #right
        (c[0], c[1]-l),  # ignored
    ]
    boundrys=[
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,
    ]
    paths = Path(coordinate, boundrys)
    patch = patches.PathPatch(paths, edgecolor=color, facecolor='none', linewidth=2.5, rasterized=1,alpha=t)
    return patch

k=5000
def trace(i,v=40,d=7):
    return (np.sin(np.pi*i/k*v-np.pi/2)*d,-np.cos(np.pi*i/k*v-np.pi/2)*d)

def revtrace(i,v=40,d=7):
    return (-np.sin(np.pi*i/k*v-np.pi/2)*d,-np.cos(np.pi*i/k*v-np.pi/2)*d)

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(40,40))

for i in range(1000000):
    v=40
    ax.cla()
    for n in range(16):
        n=n+1
        ax.add_patch(triangle(revtrace(i,v*(15+n)/16),0.8*n,'#A52C23',0.5))
    for m in range(16):
        m=m+1
        ax.add_patch(triangle(trace(i,v*(15+m)/16),0.8*m,'#F4A8C7',0.7))

    #settings for the canvas
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    plt.xticks([])
    plt.yticks([])

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Note that using time.sleep does *not* work here!
    plt.pause(0.01)