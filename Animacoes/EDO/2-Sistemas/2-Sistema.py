import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.integrate import solve_ivp

fig = plt.figure()
ax = plt.axes(xlim=(-5, 5), ylim=(-3, 3))
line1, = ax.plot([],[],lw=2)
line2, = ax.plot([],[],lw=2)

def init():
    line1.set_data([],[])
    #line2.set_data([],[])
    return line1, #line2,

def animate(i):

    def Model(t,Y):
        x,y = Y
        dxdt = -x 
        dydt = -2*y
        return [dxdt,dydt]
    
    z0 = [3,3]
    t_span = (-20,20)
    t = np.linspace(-20,20,1000)
    sol = solve_ivp(Model,t_span,z0,t_eval=t)

    x1 = sol.y[0][:i]
    y1 = sol.y[1][:i]

    # x2 = sol[1].t[:i]
    # y2 = sol[1].y[0][:i]

    line1.set_data(x1,y1)
    #line2.set_data(x2,y2)
    
    return line1,#line2

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=30, blit=True)

plt.show()