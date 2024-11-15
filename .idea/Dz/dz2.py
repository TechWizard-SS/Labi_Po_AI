import matplotlib.pyplot as plt
import numpy as np
import matplotlib.text as text
a = np.arange(0, 3.02)
b = np.arange(0, 3.02)
c = np.exp(a)
d = c[::-1]
fig, ax = plt.subplots()
plt.plot(a, c, 'k--', a, d, 'k:', a, c + d, 'k')
plt.legend(('Model length', 'Data length', 'Total message length'), loc ='upper center', shadow=True)
plt.ylim([-1, 20])
plt.grid(False)
plt.xlabel('Model complexity --->')
plt.ylabel('Message length --->')
plt.title('Minimum Message Length')
plt.show()