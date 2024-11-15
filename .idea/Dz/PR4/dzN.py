import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Физические константы
R = 0.08314  # Литр·бар/(моль·К)
a = 1.39     # Константа (пример, для CH4)
b = 0.039    # Константа (пример, для CH4)

# Данные
myT = np.array([300, 350, 400, 450])  # Температуры (K)
myV = np.linspace(0.1, 3, 100)  # Объемы (L)
myP = []

# Рассчитываем давление для каждой температуры
for T in myT:
    P = (R * T) / (myV - b) - a / (myV ** 2)  # Уравнение ван-дер-Ваальса
    myP.append(P)

# Цветовая шкала
c = np.arange(1, len(myT) + 1)
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.jet)
cmap.set_array([])

# График
plt.grid()

for i, yi in enumerate(myP):
    plt.plot(myV, yi, label=f"{myT[i]} K", c=cmap.to_rgba(i))

plt.title("van der Waals Equation of State", weight="bold")
plt.xlabel("Volume $(L)$", weight="bold")
plt.ylabel("Pressure $(bar)$", weight="bold")

# Добавление цветовой шкалы
cbar = plt.colorbar(cmap, ax=plt.gca())
cbar.set_ticks(c)
cbar.set_ticklabels(myT)
cbar.ax.set_ylabel("Temperature ($K$)", weight="bold")

plt.legend(title="Temperature ($K$)")
plt.show()
