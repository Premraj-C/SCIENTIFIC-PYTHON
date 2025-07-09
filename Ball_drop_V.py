import numpy as np
import matplotlib.pyplot as plt

#constant parameters
g = 9.81
r_o = 888
r_s = 7910
R = 0.01
V = (4*np.pi*R**3)/3
u = 3.85
w = r_s * V*g
#function for the derivative

def f(v):
    return (g-(r_o*g/r_s) - (6*np.pi*R*u*v)/(r_s*V) )

t_start = 0
t_end = 1
n = 1000
t_step = (t_end - t_start)/n

#initialize time 
t = np.arange(0,t_end+t_step, t_step)
v = np.zeros(len(t))
t0 = 0
v[t0] = 0

v_t = (r_s - r_o)*g*V/(6*np.pi*R*u)


for i in range(0,len(t)-1):
    v[i+1] = v[i] + t_step* f(v[i])
plt.plot(t,v,'-',label="Approximate_sol")
plt.plot(t, v_t*(1-np.exp(-6*np.pi*R*u*g*t/w)), '--',label="Exact_sol")
plt.pause(0.0001)
plt.grid()
plt.xlabel('time')
plt.ylabel('Velocity')
plt.legend()
plt.title('Ball dropped in a viscous fluid')
plt.show()
