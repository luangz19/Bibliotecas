import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.integrate import solve_ivp

fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(0, 15))
line, = ax.plot([],[],lw=2)

def init():
    line.set_data([],[])
    return line,

def animate(i):

    def Model(t,y):
        r = 0.1
        return r*y
    
    y0 = 2
    t_span = (0,20)
    t = np.linspace(0,20,1000)
    sol = solve_ivp(Model,t_span,[y0],t_eval=t)

    x = sol.t[:i]
    y = sol.y[0][:i]
    line.set_data(x,y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=2, blit=True)

plt.show()