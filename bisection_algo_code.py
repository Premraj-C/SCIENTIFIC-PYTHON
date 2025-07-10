#THIS IS THE ROOT FINDING ALGORITHM CALLED ''BISECTION METHOD'
import numpy as np
a = int(input("one: "))   #initial guessess
b = int(input("two: "))
#set tol value
e = 0.001       #threshold error value
#set the midpoint
iterr = 1
itermax = 50

def f(x):
    return x**2 - 5          #change here the function value for other equations

if f(a)*f(b)>0:
    print("wrong guesses given")
else:
    
     #this belw line checks iteratively, the error convergance.
    while abs((b-a)/2)> e and iterr<itermax:
        iterr = iterr+1
        m = 0.5*(a+b)     #this is the mid value obtained by bisecting the interval
        if f(m)==0:
            print("m is the root")
        
        elif f(a)*f(m)<0:
            b = m
        else:
            a = m

        print(iterr," ", m)
    
