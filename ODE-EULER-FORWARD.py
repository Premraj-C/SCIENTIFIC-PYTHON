import numpy as np
import matplotlib.pyplot as plt

#initializing the parameters
t_end = int(input("Enter the simulation time:"))
t_start = 0
n = int(input("Enter the grid no:"))
t_step = round((t_end - t_start)/n, 2)

#intialization of ode
t0 = 3
y0 = 4

#defien the function
def f(y,t):
	return -t/y
#give the max error for convergence
y_vals = []
t_vals = []
error = 1
error_threshold = 0.0001
error_arr = []
iteration = []
count = 0
while error > error_threshold:
	#i = i+1
	count = count + 1
	y_n = y0 + t_step*f(y0,t0)
	y0 = y_n
	t0 = t0+ t_step
	y_vals.append(y_n)
	t_vals.append(t0)
	y_act = np.sqrt(50 - 2*(t0)**2)
	error = abs(y_act - y_n)
	iteration.append(count)
	error_arr.append(error)
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
	


