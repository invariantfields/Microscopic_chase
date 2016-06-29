# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 21:18:28 2016

@author: Naga Teja
"""

import numpy as np
z = 10000
k = 0.2 #speed of neutrophil
t = 2 #step size of E.coli
g = np.array([1,2])
g[0] = 25 #x-coordinate
g[1] = 25 #y-coordinate
def r(a):
    r = np.sqrt(((a[0])**2)+((a[1])**2))
    return r
    
def v(a,k,t):
    p    = np.zeros(2)
    m    = np.random.rand()
    e   = m *2*np.pi
    #print(np.sin(e))
    p[1] = np.sin(e)
    p[0] = np.cos(e)
    #print(p)
    a = a*(1-k) + t*p
    return a

l = 0

p = 0

c = 0

q = np.zeros(z)

while(p < z):
    b = g
    l = 0
    while (r(b)>3):
        b = v(b,k,t)
        l = l+1
        
    c = c + l
    q[p] = l
    p = p+1
    #print(l)

print(c/z)
print(np.std(q))