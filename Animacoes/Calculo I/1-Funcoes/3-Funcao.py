import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 4))
line, = ax.plot([],[],lw=2)

def init():
    line.set_data([],[])
    return line,

def animate(i):
    x = np.linspace(0,2,1000)
    y = x**2
    x = x[:i]
    y = y[:i]
    line.set_data(x,y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=2, blit=True)

plt.show()