import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x = np.linspace(0,5,100)

# Função de Movimento
y = -x**3 + x**2 + 1

# Velocidade
dydx = -3*x**2 + 2*x

# Aceleração
d2ydx2 = -6*x + 2

plt.style.use("dark_background")
fig,ax = plt.subplots(figsize=(8,6))

ax.set_xlim(min(x),max(x)+2)
ax.set_ylim(min(y),max(y)+2)
ax.set_title(r"$f(x) =  -x^3 + x^2 + 1 $", fontsize=14)
curvas = []

for i in range(3):
    legendas = ["Função de Movimento", "Velocidade", "Aceleração"]
    lines, = ax.plot([],[], label=legendas[i])
    curvas.append(lines)

def animate(frame):
    curvas[0].set_data(x[:frame],y[:frame])
    curvas[1].set_data(x[:frame],dydx[:frame])
    curvas[2].set_data(x[:frame],d2ydx2[:frame])
    return curvas[0],curvas[1],curvas[2],

anim = animation.FuncAnimation(
    fig=fig,
    func=animate,
    frames=len(x),
    interval=55,
    blit=True
)

plt.grid(linestyle=":", alpha=0.5)
plt.legend()
anim.save("Função de Movimenro.gif")
plt.show()