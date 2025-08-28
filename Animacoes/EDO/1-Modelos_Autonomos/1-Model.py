import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def Model(t,P):
    r = 0.1
    return r*P

#

t_span = (0,10)

t = np.linspace(0,10,100)

sol = [solve_ivp(Model,t_span,[y0],t_eval=t) for y0 in [1.0,2.0]]

plt.style.use("dark_background")
plt.figure(figsize=(15,12))

for i in range(len(t)):
    plt.scatter(sol[0].t[i], sol[0].y[0][i], color="yellow",linewidths=0.1)
    plt.scatter(sol[1].t[i], sol[1].y[0][i], color="yellow",linewidths=0.1)
    plt.xlim(0,12)
    plt.ylim(0,15)
    plt.pause(0.1)



plt.show()