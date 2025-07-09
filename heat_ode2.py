#cooling of an aluminum sphere--lumped parameter method

import numpy as np
import matplotlib.pyplot as plt
#convective heat transfer coefficient
h = 890 # w/m^2-*c
c = 896 # J/kg-*c

r_al = 2707 #kg/m^3

T0 = 150  #in *c
T_inf = 20 

t_start = 0
t_end  = 3  # in seconds

t_step = 0.01
n_p = (t_end - t_start)/ t_step
R = 0.2 #radius in meters
Vol_s = 4*np.pi*R**3/3

Area_s = 4*np.pi*R**2
m_s = r_al * Vol_s    # mass in kg
tau_t = m_s*c/(h*Area_s)   #time constant tau

t = np.arange(t_start, t_end+t_step, t_step)

T = np.zeros(len(t))
T[t_start] = T0
T[t_end] = T_inf

# function for the derivative
def T_der(T):
    return (h*Area_s*(T_inf - T))/(m_s*c)


for i in range(0, len(t)-1):
    T[i+1] = T[i] + t_step* T_der(T[i])
    
plt.plot(t,T,'-',label="approx")
plt.plot(t,((T0-T_inf)*np.exp(-t/tau_t) + T_inf), '--', label="exact" )
plt.grid()
plt.xlabel('time')
plt.ylabel('temperature')
plt.title('cooling_problem_Euler_method')
plt.legend()
plt.show()
