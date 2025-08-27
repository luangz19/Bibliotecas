import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def Model(t,Y):
    x,y = Y
    dxdt = -x 
    dydt = -2*y
    return [dxdt,dydt]

#z0 = [1,2]
t_span = (-20,20)
t = np.linspace(-20,20,50)

sol = [solve_ivp(Model,t_span,z0,t_eval=t) for z0 in ([0,0],[1,2],[-1,2],[-1,-2],[1,-2])]

plt.style.use("dark_background")

for i in range(len(t)):
    plt.scatter(sol[0].y[0][i],sol[0].y[1][i],color="r", linewidths=0.1)
    plt.scatter(sol[1].y[0][i],sol[1].y[1][i],color="g", linewidths=0.1)
    plt.scatter(sol[2].y[0][i],sol[2].y[1][i],color="b", linewidths=0.1)
    plt.scatter(sol[3].y[0][i],sol[3].y[1][i],color="yellow", linewidths=0.1)
    plt.scatter(sol[4].y[0][i],sol[4].y[1][i],color="white", linewidths=0.1)
    plt.xlim(-5,5)
    plt.ylim(-3,3)
    plt.pause(0.01)

plt.show()