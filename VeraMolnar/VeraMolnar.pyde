import random

def setup():
    size(928,928)
    background(255)
    noLoop()

def draw():
    
    l0=[]
    k0=0
    for k0 in range(10):
        k0=k0+1
        a0=random.randint(0,7)
        b0=random.randint(0,7)
        c0=(a0,b0)
        l0.append(c0)
    #For red boxes
    l1=[]
    k1=0
    for k1 in range(20):
        k1=k1+1
        a1=random.randint(0,7)
        b1=random.randint(0,7)
        c1=(a1,b1)
        l1.append(c1)
    
    l1_2=[]
    k1_2=0
    for k1_2 in range(3):
        k1_2_1=random.randint(0,7)
        k1_2_2=random.randint(0,7)
        c1_2=(k1_2_1,k1_2_2)
        l1_2.append(c1_2)
    
    #For pink boxes
    l2=[]
    k2=0
    for k2 in range(10):
        k2=k2+1
        a2=random.randint(0,7)
        b2=random.randint(0,7)
        c2=(a2,b2)
        l2.append(c2)
        
    #for yellow boxes
    l3=[]
    k3=0
    for k3 in range(37):
        k3=k3+1
        a3=random.randint(0,7)
        b3=random.randint(0,7)
        c3=(a3,b3)
        l3.append(c3)
    
    #for green boxes
    l4=[]
    k4=0
    for k4 in range(26):
        k4=k4+1
        a4=random.randint(0,7)
        b4=random.randint(0,7)
        c4=(a4,b4)
        l4.append(c4)
    
    #for purple boxes
    l5=[]
    k5=0
    for k5 in range(32):
        k5=k5+1
        a5=random.randint(0,7)
        b5=random.randint(0,7)
        c5=(a5,b5)
        l5.append(c5)
    
    #for dark-blue boxes
    l6=[]
    k6=0
    for k6 in range(20):
        k6=k6+1
        a6=random.randint(0,7)
        b6=random.randint(0,7)
        c6=(a6,b6)
        l6.append(c6)
    
    #for blue boxes
    l7=[]
    k7=0
    for k7 in range(20):
        k7=k7+1
        a7=random.randint(0,7)
        b7=random.randint(0,7)
        c7=(a7,b7)
        l7.append(c7)
    
    #Draw Boxes with random distribution
    for i in range(8):
        x=100+104*i
        for j in range(8):
            y=100+104*j
            rectMode(CENTER)
            strokeWeight(2)
            
            for t0 in range(10):
                    if (i,j)==l0[t0]:
                        stroke(255)#white
                        rect(x, y, 102, 102)
                    else:
                        pass
                        
            for t1 in range(20):
                    if (i,j)==l1[t1]:
                        stroke(218,90,125)#red
                        s0=random.randint(0,1)
                        if s0==0:
                            rect(x,y,36,36)  
                        else:
                            rect(x,y,4,4)
                    else:
                        pass
            
            for t1_2 in range(3):
                    if (i,j)==l1_2[t1_2]:
                        stroke(218,90,125)#red
                        rect(x,y,100,100)  
                    else:
                        pass
            
            for t2 in range(10):
                    if (i,j)==l2[t2]:
                        stroke(209,150,172)#pink
                        s1=random.randint(0,1)
                        if s1==0:
                            rect(x, y, 92, 92)
                        else:
                            rect(x,y,36,36)  
                    else:
                        pass
            
            
            for t3 in range(37):
                    if (i,j)==l3[t3]:
                        stroke(215,183,106)#yellow
                        s2=random.randint(0,1)
                        if s2==0:
                            rect(x,y,84,84)
                        else:
                            rect(x,y,44,44)  
                    else:
                        pass
            
            for t4 in range(26):
                    if (i,j)==l4[t4]:
                        stroke(175,205,139)#green
                        s3=random.randint(0,1)
                        if s3==0:
                            rect(x,y,76,76)
                        else:
                            rect(x,y,12,12)  
                    else:
                        pass
                        
            for t5 in range(32):
                    if (i,j)==l5[t5]:
                        stroke(121,134,192)#purple
                        s4=random.randint(0,1)
                        if s4==0:
                            rect(x,y,68,68)
                        else:
                            rect(x,y,20,20)  
                    else:
                        pass
                                    
            for t6 in range(20):
                if (i,j)==l6[t6]:
                    stroke(77,149,205)#dark-blue
                    rect(x,y,60,60)
                else:
                    pass            
                    
            for t7 in range(20):
                    if (i,j)==l7[t7]:
                        stroke(136,200,206)#blue
                        s5=random.randint(0,1)
                        if s5==0:
                            rect(x,y,52,52)
                        else:
                            rect(x,y,28,28)  
                    else:
                        pass        
        
def mouseMoved():
    redraw()        
