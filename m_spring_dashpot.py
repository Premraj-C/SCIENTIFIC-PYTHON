""" python program to solve the single second order differential equation
governing the mass-spring-dashpot system using the Runge Kutta algorithm"""

import numpy as np
import matplotlib.pyplot as plt

#m = mass
#c = damping constant
#k = stiffness constant
#t_start- starting time point
#ending time point= t_end
#t_step = stepsize of time array
#y = displacement
#velocity
def spring_mass_sys(m,k,c,t_start,t_end,t_step):

	t = np.arange(t_start, t_end+t_step, t_step)
	# setting up the displace array 'y' and velocity array with initial conditions applied

	y = np.zeros(len(t))
	v = np.zeros(len(t))
	y[t_start] = 5
	v[t_start] = 0
	#function of displacement
	def f1(y,v):
	    return  (-c*v/m - k*y/m)
	#function of velocity
	def f2(v):
	    return v

	#solving through iteration
	for i in range(t_start, len(t)-1):
	    k1 = f1(y[i],v[i])
	    l1 = f2(v[i])
	    k2 = f1(y[i]+t_step*l1/2, v[i]+t_step*k1/2)
	    l2 = f2(v[i]+t_step*k1/2)
	    k3 = f1(y[i]+t_step*l2/2, v[i]+t_step*k2/2)
	    l3 = f2(v[i]+t_step*k2/2)
	    k4 = f1(y[i]+t_step*l3, v[i]+t_step*k3)
	    l4 = f2(v[i]+t_step*k3)
	    
	    y[i+1] = y[i] + t_step*(l1+ 2*(l2+l3)+ l4)/6
	    v[i+1] = v[i] + t_step*(k1+ 2*(k2+k3)+k4)/6
	    
	plt.plot(t,y, label='displacement')
	plt.plot(t,v, label= 'velocity')
	plt.xlabel('time')
	plt.ylabel('functions')
	plt.grid()
	plt.legend()
	plt.show()
	
spring_mass_sys(25,200,5,0,100,0.05)
