import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")

fig, ax = plt.subplots()

x = np.linspace(0,10,30)

y = x**2

for i in range(len(x)):
    ax.plot(x[i],y[i],"o")
    ax.set_xlim(-2,18)
    ax.set_ylim(-2,110)
    plt.pause(0.2)

plt.show()


