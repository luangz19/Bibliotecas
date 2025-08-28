import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# dydt = -2t-y

#Criando uma malha 
t,y = np.linspace(-10,10,20),np.linspace(-10,10,20)
T,Y = np.meshgrid(t,y)

# Fazendo dt = 1
DT = 1
DY = -2*T - Y

# Normalizando os vetores
M = np.sqrt(DT**2 + DY**2)

DT = DT/M
DY = DY/M

# Definindo os gráficos
plt.style.use("dark_background")
fig,axes = plt.subplots()

axes.set_xlim(min(t),max(t))
axes.set_ylim(min(y),max(y))

# Plota os vetores
axes.quiver(T,Y,DT,DY, color="yellow")

# # Defindo a animação
# def animate(frames):
#     quiver(T[:frames],Y[:frames],DT[:frames],DY[:frames])
#     return quiver

# anim = animation.FuncAnimation(
#     fig=fig,
#     func=animate,
#     #init_func=init,
#     frames=len(t),
#     interval=3,
#     blit=True
# )

plt.show()
