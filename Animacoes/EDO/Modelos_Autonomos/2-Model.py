import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

r = 0.1
K = 1000

def Model(t,P):
    return r*P*(1 - P/K)

t_span = (0,100)

t = np.linspace(0,100,100)

sol = [solve_ivp(Model,t_span,[y0],t_eval=t) for y0 in [100,500,1200]]

plt.style.use("dark_background")
plt.figure(figsize=(15,12))
plt.hlines(K,xmin=0,xmax=100)

for i in range(len(t)):
    plt.scatter(sol[0].t[i], sol[0].y[0][i], color="yellow",linewidths=0.1)
    plt.scatter(sol[1].t[i], sol[1].y[0][i], color="green",linewidths=0.1)
    plt.scatter(sol[2].t[i], sol[2].y[0][i], color="blue",linewidths=0.1)
    plt.xlim(-5,110)
    plt.ylim(-10,1400)
    plt.pause(0.1)



plt.show()