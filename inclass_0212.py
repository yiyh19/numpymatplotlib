import numpy as np
import matplotlib.pyplot as plt

np.linspace(0,10)
time = np.linspace(0,10)
y = np.sin(time)
plt.plot(time,y)
plt.xlabel('time')
plt.ylabel('y')
plt.title('y vs time')
plt.show()