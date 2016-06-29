# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 02:04:32 2016

@author: Naga Teja
"""
#import time as tm
import numpy as np
n = 2#reach of neutrophil
z = 10000#number of kills 
k =2 #speed of neutrophil
t = 2 #step size of E.coli
a = np.array([1,2])
d = 1.8 #diffusion constant
a[0] =10 #x-coordinate
a[1] = 0 #y-coordinate
de = np.zeros((5,2))
m = 1 #constant of diffusion

def shift(w,c):
    l = np.zeros((5,2))
    
    for i in range(4):
        l[i+1,] = w[i,]
    l[0,] = c
    #print(l)        
#    k = w[0,]
#    print(k)    
#    w[0,] = c
#    c = w[1,]
#    w[1,] = k
#    c = w[2,]
#    w[2,] = k
#    c = w[3,]
#    w[3,] = k
#    c = w[4,]
#    w[4,] = k
#    print(w)
    #tm.sleep(0.01)
    return(l)
 
def dif(w,a,m,d):
    o = np.zeros(2)
    for i in range(0,5):
        k = w[i,]
        t = i+1
        c = m*np.exp((-1)*r(k)**2/(4*np.pi*d*t))/((4*np.pi*t*d)**2)
        o = o + w[i,]*c
    if r(o)!= 0:
        return(o/r(o))
    else:
        return(o)        
        
              
def r(a):
    r = np.sqrt(((a[0])**2)+((a[1])**2))
    return r
    
def v(a,k,o,t):
    p    = np.zeros(2)
    m    = np.random.rand()
    e   = m *2*np.pi
    #print(np.sin(e))
    p[1] = np.sin(e)
    p[0] = np.cos(e)
    #print(p)
    a = a + t*p-k*o 
    return a

l = 0

p = 0

c = 0

q = np.zeros(z)

while(p < z):
    b = a
    l = 0
    while (r(b)>n):
        o = dif(de,a,m,d)
        b = v(b,k,o,t)
        de = shift(de,b)
        l = l+1
        #print(l)
    c = c + l
    q[p] = l
    p = p+1
    
    #print(l)

print(c/z)
print(np.std(q))
#print(q)