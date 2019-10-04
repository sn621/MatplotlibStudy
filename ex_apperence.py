import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator,FormatStrFormatter,AutoMinorLocator)
from cycler import cycler
# Color
SColors = [(246/255,170/255,0/255), (0/255,90/255,255/255), (255/255,75/255,0), (3/255,175/255,122/255), (153/255,0,153/255), (255/255,128/255,130/255), (128/255,64/255,0), (132/255,145/255,158/255), (77/255,196/255,255/255)]
plt.rcParams['axes.prop_cycle'] = cycler(color= SColors)

# Figure basics
plt.rcParams['figure.figsize'] = (8,6)
def SetFigSize(x,y):
    plt.rcParams['figure.figsize'] = (x,y)

plt.rcParams['savefig.transparent'] = False
plt.rcParams['savefig.dpi'] = 300

# Fonts
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 15
def SetFontSize(size):
    plt.rcParams['font.size'] = size

plt.rcParams['axes.labelsize'] = 20
def SetLabelSize(size):
    plt.rcParams['axes.labelsize'] = size

# plt.rcParams['xtick.labelsize'] = 15
# plt.rcParams['ytick.labelsize'] = 15

# Grid
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.8

lwidth = 1.5
# plt.rcParams['axes.linewidth'] = lwidth
# def SetAxesWidth(width):
    # plt.rcParams['axes.linewidth'] = width

# X ticks
plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['xtick.major.width'] = lwidth
# def SetTickXWidth(width):
    # plt.rcParams['xtick.major.width'] = width

plt.rcParams['xtick.minor.visible'] = True
plt.rcParams['xtick.major.size'] = 8
plt.rcParams['xtick.minor.size'] = 4

# Y ticks
plt.rcParams['ytick.direction'] = 'in'
# plt.rcParams['ytick.major.width'] = lwidth
# def SetTickYWidth(width):
    # plt.rcParams['ytick.major.width'] = width

plt.rcParams['ytick.minor.visible'] = True
plt.rcParams['ytick.major.size'] = 8
plt.rcParams['ytick.minor.size'] = 4

# linewidth
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['patch.linewidth'] = 2
plt.rcParams['lines.markersize'] = 5
