import group_plotting_standard as gps
import numpy as np
import pylab as plt

x = np.linspace(0,1,100)
y = np.sin(2*np.pi*x)


plt.figure(1)
ax1=plt.subplot(1,1,1)
#gps.rgscatter(x,y,pkwargs={'s':100,'marker':'*'},fill=True)
gps.rgplot(x,y,pkwargs={'linewidth':2},type='dot')

ax1.minorticks_on()
plt.xlabel(r'$\chi$')
plt.ylabel('Y')
plt.axhline(0.0, linestyle='--',linewidth=1, color='b', dashes = (10,10))

plt.tight_layout()
plt.savefig('test.png')
plt.show()