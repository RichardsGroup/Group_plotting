import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import re

#GTR Don't really know what this does
#JT: This will set the figure size such that it will line up with the text in a LATEX document. I'm not sure it is strictly necessary for pdf's because they should scale properly. This function is used to define the size in the image below, though. To generate a square image you would need to input something like : figsize(0.9,0.9). I typically set the figure size when I define the frame though, so again, its an optional function
def figsze(hscale, 
	        vscale=(np.sqrt(5.0)-1.0)/2.0,
            fig_width_pt = 504.0):
   

    """
    Get the fig_width_pt by inserting \the\textwidth into LaTeX document.

    hscale is fraction of text width you want.

    vscale is fraction of hscale (defaults to golden ratio)  
    """
   
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    fig_width = fig_width_pt*inches_per_pt*hscale   # width in inches
    fig_height = fig_width*vscale                   # height in inches
    fig_size = [fig_width,fig_height]
    return fig_size

###### RC PARAMETERS FOR MATPLOTLIB######

pgf_with_latex = {                      # setup matplotlib to use latex for output
	"axes.linewidth":2.0,
    #"pgf.texsystem": "pdflatex",        # change this if using xetex or latex
    "font.family": "sans-serif",
    "font.sans-serif": ['Helvetica'],         # blank entries should cause plots to inherit fonts from the document
    "text.usetex": True,                # use LaTeX to write all text
   	"axes.unicode_minus": False,		#Use ASCII Hyphen instead of unicode minus sign
    "axes.labelsize": 24,               # LaTeX default is 10pt font.
    "axes.labelpad" : 12,				# Distance between label and axis
    "axes.formatter.limits":[-5, 5],	# use sci notation if log10 of axis range is smaller than first or larger than second 
    "axes.formatter.useoffset":False,
    "axes.labelsize": 20,
    "legend.fontsize": 18,               # Make the legend/label fonts a little smaller
    "xtick.labelsize": 24,
    "ytick.labelsize": 24,
    'xtick.major.width':1, 
    'xtick.minor.width':1, 
    'ytick.major.width':1, 
    'ytick.minor.width':1, 
    'xtick.major.size':18, 
    'xtick.minor.size':9, 
    'ytick.major.size':18, 
    'ytick.minor.size':9,
    'xtick.major.pad':8,
    'ytick.major.pad':8,
    "figure.figsize": figsze(1,1),     # default fig size of 0.9 textwidth
   # "pgf.preamble": [
    #    r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it
        #r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
     #   r"\DeclareUnicodeCharacter{2212}{$-$}"
      #  ]
    }

mpl.rcParams.update(pgf_with_latex)





### PLOT COMMANDS#####


## NEW SCATTERPLOT#####

def rgscatter(x,y,pkwargs={},fill=True):
	pkwargs.setdefault('marker', '.')
	pkwargs.setdefault('s', 1)
	pkwargs.setdefault('color', 'k')
	if fill== False:
		pkwargs.setdefault('facecolors', 'none') #Make open points
	if fill==True:
		pkwargs.setdefault('edgecolors', 'none') #Get rid of edge colors	
	P = plt.scatter(x,y,**pkwargs)
	
	return P
	


## NEW LINE PLOT#####

def rgplot(x,y,pkwargs={},type = 'solid'):
	pkwargs.setdefault('linewidth', 2)
	pkwargs.setdefault('color', 'k')
	if type == 'dot-dash':
		pkwargs.setdefault('dashes', (3,5,10,5))
	if type == 'dash-dot':
		pkwargs.setdefault('dashes', (3,5,10,5))
	if type == 'dash':
		pkwargs.setdefault('dashes', (10,10))
	if type == 'dot':
		pkwargs.setdefault('dashes', (1,3,1,3))
	
	
	
	P = plt.plot(x,y,**pkwargs)
	return P
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	