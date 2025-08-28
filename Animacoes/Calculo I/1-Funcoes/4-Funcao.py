import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x = np.linspace(0,5,100)

y = np.exp(x)

plt.style.use("dark_background")
fig,ax = plt.subplots()
ax.set_xlim(min(x),max(x))
ax.set_ylim(min(y),max(y))

line, = ax.plot([],[],"--",lw=2)

def update(frame):
    line.set_data(x[:frame],y[:frame])
    return line,

anim = animation.FuncAnimation(
    fig=fig,
    func=update,
    frames=len(x),
    interval=45,
    blit=True
)

plt.show()