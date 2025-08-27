import numpy as np
import matplotlib.pyplot as plt

# Cor do 
plt.style.use("dark_background")

fig, ax = plt.subplots()

f = lambda x: x**2

x = np.linspace(0,3,40)

ax.plot(x,f(x), label="f(x) = x")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.legend()


# Plotando as partições,no intervalo [0,3] com 39 subintervalos
for i in range(40):
    ax.vlines(x[i], ymin=0, ymax=f(x[i]))
    plt.pause(0.2)
 
plt.show()
