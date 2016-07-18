###############
### TIMLIN 2016 FIGURE 15 PLOTTING ROUTINE
###############	
#Useful imports
import group_plotting_standard
import os
import sys
#sys.path.insert(0, '/Users/gtr/Dropbox/research/spitzer/2014/qlf/densityplotmaster/densityplot/')
sys.path.insert(0, '/Users/johntimlin/densityplot/densityplot')

#import densityplot
from densityplot.hex_scatter import hex_contour as hex_contour
import densityplot.hex_scatter as hex_scatter

#import hex_contour
#import hex_scatter
from astropy.io import fits as pf

import numpy as np
from scipy import stats
from pylab import plt
#from plotting import scatter_density
import astropy.io.ascii as ascii
#import brewer2mpl
import palettable
from matplotlib.ticker import MultipleLocator, FormatStrFormatter



#GTR Why is this separate?
#JT: It doesn't have to be separate, I suspect that it only is because it gets changed a lot more frequently
#plt.rc("axes", linewidth=3.0)

#Set up colors using palettable instead
sc = palettable.colorbrewer.qualitative.Set2_8.mpl_colors

#W1 line function
col = np.linspace(-4,4,100)
ch2prime = 20.5-col

print "plotting"

#tdata = Table.read('GTR-ADM-QSO-ir-testhighz3fall_kdephotoz_lup_trainingset_qsos_colors.dat', format='ascii') #high-z quasar colors

tdata = pf.open('GTR-ADM-QSO-ir-testhighz_kdephotoz_lup_2014_trainingset_qsos.fits')[1].data

fig=plt.figure(2,figsize=[10.0,10.0])
ax2=plt.subplot(1,1,1)

majorLocator = MultipleLocator(1)
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator(0.25)




#SpIES DATA
#hex_contour(s5color,s5mag2, levels=[0.99,0.95,0.9,0.7,0.5,0.3,0.1], std=True, min_cnt=50, smoothing=2, hkwargs={'gridsize':100,'extent':(-4,4,13,27)}, skwargs={'color':Sps,'alpha':0.1,'marker':'.'}, ckwargs={'colors':Spc,'alpha':1,'linewidths':2})
#Star DATA
#hex_contour(irstarcolor,ch2starmag, levels=[0.99,0.95,0.9,0.7,0.5,0.3,0.1], std=True, min_cnt=10, smoothing=4, hkwargs={'gridsize':50}, skwargs={'color':sts,'alpha':0.1,'marker':'.'}, ckwargs={'colors':stc,'alpha':1,'linewidths':2})
#Low-Redshift Quasars
#hex_contour(irlzcolor,ch2lzmag, levels=[0.95,0.9,0.7,0.5,0.3,0.1], std=True, min_cnt=10, smoothing=2, hkwargs={'gridsize':25}, skwargs={'color':lzs,'alpha':0.1,'marker':'.'}, ckwargs={'colors':lzc,'alpha':1,'linewidths':2})

#GTR: Don't hard code the levels.  Generate them automatically.
#JT: Something like this???

levels = np.arange(0.1,1.0,0.2)


#High Redshift Quasars 
#hex_contour(tdata['col1'],tdata['col2'], levels=[0.1,0.3,0.5,0.7,0.9,0.95], std=True, min_cnt=10, smoothing=4, hkwargs={'gridsize':10}, skwargs={'color':sc[0],'alpha':0.1,'marker':'.'}, ckwargs={'colors':[sc[0],sc[0],sc[0]],'alpha':1,'linewidths':2})

#hex_contour(tdata.s1s2,tdata.s2mag, levels=levels, std=True, min_cnt=10, smoothing=4, hkwargs={'gridsize':10}, skwargs={'color':sc[0],'alpha':0.5,'marker':'.'}, ckwargs={'colors':[sc[0],sc[0],sc[0]],'alpha':1,'linewidths':2})


'''
#GTR: Is something like this better:
#JT: It is essentially the same thing. The levels are more intuitive in hex_contour (it does percentages, I cant figure out how plt.contour does it...).  This is a good option for people who have not downloaded the density plot package though

m1 = tdata.s1s2
m2 = tdata.s2mag
xmin = m1.min()
xmax = m1.max()
ymin = m2.min()
ymax = m2.max()

X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])
values = np.vstack([m1, m2])
kernel = stats.gaussian_kde(values)
    
Z = np.reshape(kernel(positions).T, X.shape)
CS = plt.contour(X,Y,Z, levels=levels, colors=[sc[-1]])

threshold = CS.levels[0]

z = kernel(values)

# mask points above density threshold
x = np.ma.masked_where(z > threshold, m1)
y = np.ma.masked_where(z > threshold, m2)

# plot unmasked points
plt.scatter(x, y, c='grey', edgecolor='None', s=3, label='SDSS DR7' )
'''
#OLD CODE

hex_contour(tdata.s1s2,tdata.s2mag, levels=levels, std=True, min_cnt=10, smoothing=4, hkwargs={'gridsize':10}, skwargs={'color':sc[0],'alpha':0.5,'marker':'.'}, ckwargs={'colors':[sc[0],sc[0],sc[0]],'alpha':1,'linewidths':2})
#Plot points off of the axes for the legend
#plt.plot(100,101, '.', color=Sps, label='SpIES')
#plt.plot(100,101, '.', color=sts, label='Stars')
#plt.plot(100,101, '.', color=lzs, label='z<2.2 QSOs')
plt.plot(100,101, '.', color=sc[0], label=r'3.5$\textless$ z $\textless$ 5 QSOs')
#Plot Assef 2013 BOX
WISE,=plt.plot([0.119,4],[18.402,18.402], color='k',linestyle='--',linewidth=1, dashes = (10,10))
plt.plot([0.119,0.119],[0,18.402],color='k',linestyle='--',linewidth=1, dashes = (10,10))
#Plot the W1 5 sigma line in this color space
W1,=plt.plot(col,ch2prime, color='k',linestyle='-.',linewidth=1, dashes = [8,4,2,4])
#SpIES 5sigma line (CH2)
plt.axhline(22.0, linestyle='--',linewidth=1, color='b', dashes = (10,10),label=r'SpIES 5$\sigma$')

plt.xlabel(r'[3.6]$-$[4.5] Color')
plt.ylabel('[4.5]')
first_legend = plt.legend([WISE,W1],['Assef et al. 2013 limits',r'WISE W1 5$\sigma$'],loc=1)
ax = plt.gca().add_artist(first_legend)
plt.legend(loc=2,markerscale=2, scatterpoints=1)
fig.set_size_inches(10.0,10.0)
ax2.minorticks_on()

ax2.yaxis.set_major_locator(majorLocator)
ax2.yaxis.set_major_formatter(majorFormatter)
ax2.yaxis.set_minor_locator(minorLocator)
#ax2.yaxis.set_minor_formatter(majorFormatter)
label = ax2.get_yticks()
plt.yticks(label,rotation=90)

plt.xlim(-4,4)
plt.ylim(13,23)


plt.gca().invert_yaxis()

#plt.savefig('Group_Plotting2.pdf')

plt.show()
