import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]

plt.plot(x,y, color='green', marker='o', markersize=7)
plt.ylabel('Ось x')
plt.title('Первый график')
plt.show()