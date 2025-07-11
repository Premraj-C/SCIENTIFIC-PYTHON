import numpy as np
import matplotlib.pyplot as plt

#initializing the parameters
t_end = int(input("Enter the simulation time:"))              #total simulation time
t_start = 0                                         #start time
n = int(input("Enter the grid no:"))                  #number of mesh points
t_step = round((t_end - t_start)/n, 2)                #time step

#intialization of ode as per the problem
t0 = 3                                 
y0 = 4

                                              #define the function
def f(y,t):
	return -t/y
#give the max error for convergence
y_vals = []                               #empty arrays to store the values appended by the loop
t_vals = []
error = 1                              #initialize error to be 1
error_threshold = 0.0001                  #max error
error_arr = []
iteration = []
count = 0
while error > error_threshold:
	#i = i+1
	count = count + 1
	y_n = y0 + t_step*f(y0,t0)               #EUler forward formualae----> dy/dt = -t/y  --->expressed as the finite difference form
	y0 = y_n
	t0 = t0+ t_step                             #update the time from t0 to forward untill through the full nodal points
	y_vals.append(y_n)
	t_vals.append(t0)
	y_act = np.sqrt(50 - 2*(t0)**2)                   #this is the actual function of the differential equation when solved analytically!!
	error = abs(y_act - y_n)                           #error as the difference of actual to the numerical estimate
	iteration.append(count)
	error_arr.append(error)
#PLotting of both functional values and error degradation in two seperate subplots using matplotlib.
plt.subplot(1,2,1)
plt.plot(t_vals,y_vals,marker='o', label='Numerical y(t)')
plt.xlabel('y_values')
plt.ylabel('time')
plt.title('NUMERICAL SOLVER')

plt.subplot(1,2,2)
plt.plot(iteration, error_arr, color='red', marker='x', label='Error')
plt.xlabel('iteration')
plt.ylabel('error')
plt.title('Error-record')
plt.show()
plt.show()
	


