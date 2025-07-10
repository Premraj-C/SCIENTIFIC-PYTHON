"""A boy on a snowboard slides down a smooth hill, affected by the air drag modeling and simulation in python"""

import numpy as np
import matplotlib.pyplot as plt

area = 0.5 #frontal area of the skater board
c_d = 1
rho = 1.225   #density of air
theta = 15    #angle in degrees
w = 650       #weight of the boy
mue = 0.05    #coefficient of friction
#grid parameters
t_start = 0
t_end = 60     #time in seconds
dt = 0.10
N = w*np.cos(theta)
fr = mue*N
time = np.arange(t_start, t_end+dt, dt)

x = np.zeros(len(time))
v = np.zeros(len(time))

x[0] = 0
v[0] = 0
# functions of dervatives

def f(time, v):
    return (w*np.sin(theta)-fr- (c_d * rho*v**2)/2 )

def g(v):
    return v
for i in range(t_start, len(time)-1):
    
    k1 = f(time[i], v[i])
    l1 = g(v[i])
    k2 = f(time[i]+dt/2, v[i]+dt*k1/2)
    l2 = g(v[i]+dt*k1/2)
    k3 = f(time[i]+dt/2, v[i]+dt*k2/2)
    l3 = g(v[i]+dt*k2/2)
    k4 = f(time[i]+dt, v[i]+dt*k3)
    l4 = g(v[i]+dt*k3)
    
    x[i+1] = x[i]+  dt*(k1+2*(k2+k3)+k4)/6 
    v[i+1] = v[i] + dt*(l1+2*(l2+l3)+l4)/6
    
plt.plot(time,x, label='displacement')
plt.plot(time, v, label='velocity')
plt.xlabel('time')
plt.ylabel('functions')
plt.grid()
plt.legend()
plt.show()
