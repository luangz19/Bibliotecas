import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.integrate import solve_ivp


def Model(t,Y):
        x,y = Y
        dxdt = -x 
        dydt = -2*y
        return [dxdt,dydt]
    
#z0 = [3,3]
t_span = (-20,20)
t = np.linspace(-20,20,1000)
sol = [solve_ivp(Model,t_span,z0,t_eval=t) for z0 in [(1,2),(-1,2),(1,-2),(-1,-2)]]
       
plt.style.use("dark_background")
fig = plt.figure()
ax = plt.axes(xlim=(-5, 5), ylim=(-3, 3))

line1, = ax.plot([],[],color="r",lw=2)
line2, = ax.plot([],[],color="g",lw=2)
line3, = ax.plot([],[],color="b",lw=2)
line4, = ax.plot([],[],color="yellow",lw=2)

def init():
    line1.set_data([],[])
    line2.set_data([],[])
    return line1,line2,line3,line4,

def animate(frames):
    x1 = sol[0].y[0][:frames]
    y1 = sol[0].y[1][:frames]

    x2 = sol[1].y[0][:frames]
    y2 = sol[1].y[1][:frames]

    x3 = sol[2].y[0][:frames]
    y3 = sol[2].y[1][:frames]

    x4 = sol[3].y[0][:frames]
    y4 = sol[3].y[1][:frames]

    line1.set_data(x1,y1)
    line2.set_data(x2,y2)
    line3.set_data(x3,y3)
    line4.set_data(x4,y4)
    
    return line1,line2,line3,line4,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(t), interval=30, blit=True)

plt.show()