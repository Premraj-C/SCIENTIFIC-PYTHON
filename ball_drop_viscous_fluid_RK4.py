import numpy as np
import matplotlib.pyplot as plt

#constant parameters
g = 9.81                       #acceleration due to gravity
r_o = 888                      #density of oil- SI units
r_s = 7910                     #density of sphere- SI units
R = 0.01                        #Radius of sphere in [metres]
V = (4*np.pi*R**3)/3               #volume of sphere
u = 3.85                          #dynamic viscousity - N-S/m^2
w = r_s * V*g                           #weight of sphere

#define a function for the derivative
def f(v,t):
    return (g-(r_o*g/r_s) - (6*np.pi*R*u*v)/(r_s*V) )
    
#discretization of time domain
t_start = 0
t_end = 1
n = int(input("grid_num: "))
t_step = (t_end - t_start)/n

#initialize time and velocity arrays
t = np.arange(0,t_end+t_step, t_step)   #this method arranges values from 0 to end
v = np.zeros(len(t))                  # this makes an array of zeros initially
t0 = 0
v[t0] = 0

v_t = (r_s - r_o)*g*V/(6*np.pi*R*u)               #terminal velocity is given by this formulae

#THE DIFFERENTIAL EQUATION dv/dt = [g- rho_oil/rho_steelball - (6*pi*R*mu*V)/rho_steel*volume ] USING FOURTH ORDER "RUNGE KUTTA" METHOD 
for i in range(0,len(t)-1):
    k1 = f(v[i],t[i])
    k2 = f(v[i]+t_step/2, t[i]+t_step*k1/2)
    k3 = f(v[i]+t_step/2, t[i]+t_step*k2/2)
    k4 = f(v[i]+t_step, t[i]+t_step*k3)
    
    v[i+1] = v[i] + t_step*(k1+2*(k2+k3)+k4)/6
plt.plot(t,v,'-',label="Approximate_sol")
plt.plot(t, v_t*(1-np.exp(-6*np.pi*R*u*g*t/w)), '--',label="Exact_sol")
plt.grid()
plt.xlabel('time')
plt.ylabel('Velocity')
plt.legend()
plt.title('Ball dropped in a viscous fluid')
plt.show()
