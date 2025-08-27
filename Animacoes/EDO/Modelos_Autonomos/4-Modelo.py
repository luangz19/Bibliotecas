import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.integrate import solve_ivp

fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(0, 15))
line1, = ax.plot([],[],lw=2)
line2, = ax.plot([],[],lw=2)

def init():
    line1.set_data([],[])
    line2.set_data([],[])
    return line1,line2,

def animate(i):

    def Model(t,y):
        r = 0.1
        return r*y
    
    #y0 = 2
    t_span = (0,20)
    t = np.linspace(0,20,1000)
    sol = [solve_ivp(Model,t_span,[y0],t_eval=t) for y0 in [1,2]]

    x1 = sol[0].t[:i]
    y1 = sol[0].y[0][:i]

    x2 = sol[1].t[:i]
    y2 = sol[1].y[0][:i]

    line1.set_data(x1,y1)
    line2.set_data(x2,y2)
    
    return line1,line2,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=2, blit=True)

plt.show()