import numpy as np
import matplotlib.pyplot as plt

def fr(x): return np.exp(x)
#Forward Euler method overshoot
def f_de_f(dx, x, y): 
    return 1 + y**0.5 
#Backward Euler method undershoot
def f_de_b(dx, x, y): 
    dy = 0
    dy = 1 + y**0.5
    yn += dy #predict next point 
    dyn = dx * y2n #next point derivative
    return  

def test(a=0.0, b=10.0, slot=1000):
    dx = (b - a)/slot # AU
    slot = slot + 1 #
    xs = np.empty(slot)
    y1s = np.empty(slot)
    y2s = np.empty(slot)
    err1 = np.empty(slot)
    err2 = np.empty(slot)
    err3 = np.empty(slot)
    x = a
    y2 = 1
    y2n = 0
    i = 0
    

    while x <= b:        
        xs[i] = x
        y1s[i] = fr(x) #standard curve
        y2s[i] = y2 # DE curve         
        err1[i] = y2s[i]-y1s[i] #local error
        
        dy2_c = f_de_f(dx, x, y2) #current point derivative
        dy2_n = f_de_b(dx, x, y2) #next point derivative
        #dy2 = (dy2+dy2n)/2
        
        y2 += dy2
        
        x += dx
        i += 1

    print "dx = ", dx, "slot = ", slot
    Error_global= y2s[slot-1]-y1s[slot-1]
    print "global err at {}: {:.2f}%".format(b, Error_global) 
    print "abs err at {}: {:.2f}%".format(b, abs(Error_global)) 
    print "ref err max {:.2f}%".format(max(abs(max(err1)),abs(min(err1)))/y1s[slot-1]*100) 
    
    plt.figure(1)
    plt.plot(xs,y1s) #ref 
    plt.plot(xs,y2s)    #simulate
    #plt.plot(xs,err1)
    #plt.plot(xs,err2)
    #plt.plot(xs,err3)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    
        
#main
test()
    
    