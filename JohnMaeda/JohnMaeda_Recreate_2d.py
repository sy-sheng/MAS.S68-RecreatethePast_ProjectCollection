import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
plt.axis('off')
color=["#E4007F", "#FFF100", "#0099D9", "#5A595F"]

#background points
b=0
for b in range(100):
    backells=Ellipse(xy=np.random.randint(-45,45),width=20, height=20, angle=0,color=np.random.choice(color),alpha=0.8)
    b=b+1

#gradual changing points
ri=22
ran=38
startpoint=-28

for m in range(5):
    ran=ran+2
    ri=ri-4*m
    m=m+1
    startpoint=startpoint-4
    i=startpoint
    # copy the lists
    for l in range(ran):
        i=i+2
        l=l+1
        #creat the lists
        for k in range(60):
            j=np.random.normal(0, 40)
            r=0.1*np.random.normal(ri,10)/(np.abs(j)*0.1+1)            
            ells=Ellipse(xy=(i,j), width=r, height=r, angle=0, facecolor=np.random.choice(color),edgecolor=None, alpha=0.7)
            ax.add_patch(ells)
            k=k+1


plt.show()


