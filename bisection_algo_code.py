#choosing an interval
import numpy as np
a = int(input("one: "))
b = int(input("two: "))
#set tol value
e = 0.001
#set the midpoint
iterr = 1
itermax = 50
root = np.sqrt(5)

def f(x):
    return x**2 - 5

if f(a)*f(b)>0:
    print("wrong guesses given")
else:
    

    while abs((b-a)/2)> e and iterr<itermax:
        iterr = iterr+1
        m = 0.5*(a+b)
        if f(m)==0:
            print("m is the root")
        
        elif f(a)*f(m)<0:
            b = m
        else:
            a = m

        print(iterr," ", m)
    
