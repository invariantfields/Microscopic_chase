# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:52:34 2016

@author: Naga Teja
"""

import numpy as np
n = 2#reach of neutrophil
z = 50#number of kills 
k = 6 #speed of neutrophil
t = 2 #step size of E.coli
a = np.array([1,2])
d = 0.3 #diffusion constant
a[0] = 10 #x-coordinate
a[1] = 0 #y-coordinate
de = np.zeros((5,2))
m = 0.3 #constant of diffusion

def shift(w,c):
    l = np.zeros((5,2))
    
    for i in range(4):
        l[i+1,] = w[i,]
    l[0,] = c
    return(l)
 
def dif(w,a,m,d):
    o = np.zeros(2)
    for i in range(0,5):
        k = w[i,]
        t = i+1
        c = m*np.exp((-1)*r(k)**2/(4*np.pi*d*t))/(4*np.pi*t*d)
        o = o + w[i,]*c
    if r(o)!= 0:
        return(o/r(o))
    else:
        return(o)        

def get(w,a,m,d): 
    l = 0
    o = 0
    for i in range(0,5):
        k = w[i,]
        t = i+1
        c = m*np.exp((-1)*r(k)**2/(4*np.pi*d*t))/(4*np.pi*t*d)
        o = o + c
        if k[1] !=0 and k[0] != 0:
            l = l+1/t
    if l == 0 : 
        return(0)
    else:
        return(o*4*np.pi/(m*l))
        
              
def r(a):
    r = np.sqrt(((a[0])**2)+((a[1])**2))
    return r
    
def v(a,k,o,t,d):
    p    = np.zeros(2)
    m    = np.random.rand()
    e   = m *2*np.pi
    #print(np.sin(e))
    p[1] = np.sin(e)
    p[0] = np.cos(e)
    #print(p)
    a = a + t*p
    m    = np.random.rand()
    e   = m *2*np.pi
    #print(np.sin(e))
    p[1] = np.sin(e)
    p[0] = np.cos(e)
    a = a - d*k*o + (1-d)*k*p  
    return a

l = 0

p = 0

c = 0

q = np.zeros(z)

g = 0 

while(p < z):
    b = a
    l = 0
    while (r(b)>n):
        o = dif(de,a,m,d)
        g = get(de,a,m,d)
        b = v(b,k,o,t,g)
        de = shift(de,b)
        l = l+1
        print(l)
    c = c + l
    q[p] = l
    p = p+1
    #print(l)

print(c/z)
print(np.std(q))
#print(q)