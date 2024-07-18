
#Forward Euler for single varaibles solve Differential Equation: dy/dx=3y
import numpy as np
import matplotlib.pyplot as plt

def F(y):
    return 3*y 

#Forward Euler Function
def Forward_Euler(y0,F,ti,tf,h):
    x=np.array([y0])
    t_int=np.array([ti])
    y_prev=y0

    while (ti<tf):
        y_next=y_prev+h*F(y_prev)#eulers formula
        y_prev=y_next
        x=np.append(x,y_next)#storing data points
        ti=ti+h
        t_int=np.append(t_int,ti)#storing time steps
    return x,t_int

#Actual Differential Solution
def y(x):
    return 2*np.exp(3*x)
    
    


y0=2
Y,T=Forward_Euler(y0,F,0,5,0.01)
Y_actual=y(T)
#Ploting Solution(s):

plt.plot(T,Y,color="red",label="approx") #Approximate Solution in red
plt.plot(T,Y_actual,color="blue",label="actual") #actual Solution in blue

plt.title("Forward Euler Method")
plt.xlabel("Time")
plt.ylabel("Solution")
plt.grid(True)
plt.show()









