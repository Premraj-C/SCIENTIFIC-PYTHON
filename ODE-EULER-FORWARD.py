import numpy as np
import matplotlib.pyplot as plt

#ODE SOLVEER USING EULER FORWARD METHOD
#CONSIDER THE IVP dy/dx = -x*y +13, y(0) = 0.6

#discretizing the domain
x_n = 3    #domain length
x_0 = 0   
n = int(input("Please input grid number:") )    #domain starting point
h = (x_n - x_0)/n            #space step, n= number of grid points

#function set up
def f(y,x):
    return -y*x + 13
#intialization  as given y{3} = 4 
x0 = 0
y0 = 0.6
#store the new values into this empty new arrays
X = []
Y = []
#solver loop for calculating the y values
#since it is an explicit scheme, it uses the previous value to estimate the forward value
for i in range(n):
    y_n = y0 + h*f(y0,x0)
    y0 = y_n
    x0 = x0 + h
    X.append(x0)
    Y.append(y_n)
#plotting the values
plt.plot(X,Y)
plt.title('ODE-SOLVER')
plt.xlabel('TIME-[SECONDS]')
plt.ylabel('Y-[PARAMETER]')
plt.show()
