import group_plotting_standard
import numpy as np
import pylab as plt

x = np.linspace(0,1,100)
y = np.sin(2*np.pi*x)


plt.figure(1)
ax1=plt.subplot(1,1,1)
plt.plot(x,y)
ax1.minorticks_on()
plt.axhline(0.0, linestyle='--',linewidth=1, color='b', dashes = (10,10))
plt.show()