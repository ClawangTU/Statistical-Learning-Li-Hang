import os.path
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as mTicker
from matplotlib.font_manager import FontProperties
from cycler import cycler
import pandas as pd


# default figure output configuration.
def figDefault(figSize=[7, 6], lineLw=0.5, lineMew=0.5, lineMS=2.0, axLw=0.5,
               axLs=8, tickLs=6, lgFs=8, colorOrder=None):
    # figSize: size of figure to be output.
    # lineLw: linewidth for line plot.
    # lineMew: markeregde width for line plot.
    # lineMs: marker size for line plot.
    # axLw: axes linewidth.
    # axLs: axes label size (i.e. fontsize for axes labels).
    # tickLs: axes ticks label size (i.e. fontsize for tick labels).
    # lgFs: fontsize for legends.

    # Initialize plot configuration.
    mpl.rcdefaults()

    # Line color orders.
    colorOrder0 = np.array([[58, 109, 250],
                            ]) / 255

    colorOrder1 = np.array([[58, 109, 250],
                            [255, 150, 24],
                            [0, 173, 79],
                            [237, 27, 58],
                            [112, 0, 252]]) / 255

    colorOrder2 = np.array([[41, 112, 255],
                            [255, 150, 24],
                            [33, 146, 49],
                            [237, 0, 0],
                            [231, 186, 16],
                            [156, 85, 173],
                            [82, 89, 107],
                            [237, 27, 58], ]) / 255

    ColorOrder3 = np.array([[90, 90, 90],
                            [199, 2, 22]]) / 255

    colorDict = {0: colorOrder0, 1: colorOrder1, 2: colorOrder2, 3: ColorOrder3}
    if colorOrder is None:
        colorOrder = colorOrder1
    else:
        colorOrder = colorDict[colorOrder]

    # Default plot setting.
    mpl.rcParams['axes.linewidth'] = axLw
    mpl.rcParams['axes.labelsize'] = axLs
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['savefig.dpi'] = 300
    mpl.rcParams['figure.figsize'] = np.array(figSize) / 2.54
    mpl.rcParams['figure.frameon'] = False
    mpl.rcParams['legend.fancybox'] = False
    mpl.rcParams['legend.fontsize'] = lgFs
    mpl.rcParams['legend.edgecolor'] = 'k'
    mpl.rcParams['legend.framealpha'] = 1
    mpl.rcParams['legend.labelspacing'] = 0.2
    mpl.rcParams['lines.linewidth'] = lineLw
    mpl.rcParams['lines.markeredgewidth'] = lineMew
    mpl.rcParams['lines.markersize'] = lineMS
    mpl.rcParams['savefig.format'] = 'svg'
    mpl.rcParams['savefig.frameon'] = False
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['xtick.labelsize'] = tickLs
    mpl.rcParams['xtick.top'] = True
    mpl.rcParams['xtick.major.width'] = axLw
    mpl.rcParams['xtick.major.size'] = 3
    mpl.rcParams['xtick.minor.width'] = axLw / 2
    mpl.rcParams['xtick.minor.size'] = 3 / 2
    mpl.rcParams['ytick.direction'] = 'in'
    mpl.rcParams['ytick.labelsize'] = tickLs
    mpl.rcParams['ytick.right'] = True
    mpl.rcParams['ytick.major.width'] = axLw
    mpl.rcParams['ytick.major.size'] = 3
    mpl.rcParams['ytick.minor.width'] = axLw / 2
    mpl.rcParams['ytick.minor.size'] = 3 / 2
    mpl.rcParams['axes.prop_cycle'] = cycler(color=colorOrder)


# figure putput.
def figPrint(figName, fmt='svg', ax=None, fig=None, figSize=None,
             lineLw=None, axLw=None, axLs=None, tickLs=None, lgFs=None,
             xLim=None, yLim=None, xTicks=None, yTicks=None,
             xMajorTickFormat=None, yMajorTickFormat=None,
             xMinorLocator=None, yMinorLocator=None,
             xLabel=None, yLabel=None, legend=None, lgStyle='row',
             fontFile=None, disp=True, save=True):
    # Read None variables from global configuration.
    if figSize is None:
        figSize = np.array(mpl.rcParams['figure.figsize']) * 2.54
    if lineLw is None:
        lineLw = mpl.rcParams['lines.linewidth']
    if axLw is None:
        axLw = mpl.rcParams['axes.linewidth']
    if axLs is None:
        axLs = mpl.rcParams['axes.labelsize']
    if tickLs is None:
        tickLs = mpl.rcParams['xtick.labelsize']
    if lgFs is None:
        lgFs = mpl.rcParams['legend.fontsize']
    if fmt is None:
        fmt = mpl.rcParams['savefig.format']

    # Default font: Helvetica.
    # Use Arial as substitution.
    defaultFontFile = [r'C:\windows\fonts\Helvetica.ttf'] * 3
    mpl.rcParams['font.sans-serif'] = 'Arial'

    if isinstance(fontFile, str):
        axLf, tickLf, lgF = [fontFile] * 3
    elif isinstance(fontFile, list):
        if len(fontFile) == 1:
            axLf, tickLf, lgF = fontFile * 3
        elif len(fontFile) == 3:
            axLf, tickLf, lgF = fontFile
        else:
            axLf, tickLf, lgF = [fontFile[0]] * 3
    else:
        axLf, tickLf, lgF = defaultFontFile

    if os.path.exists(axLf):
        fontAxLs = FontProperties(fname=axLf, size=axLs)
    else:
        fontAxLs = FontProperties(family='sans-serif', size=axLs)

    if os.path.exists(tickLf):
        fontTickLs = FontProperties(fname=tickLf, size=tickLs)
    else:
        fontTickLs = FontProperties(family='sans-serif', size=tickLs)

    if os.path.exists(lgF):
        fontLgFs = FontProperties(fname=lgF, size=lgFs)
    else:
        fontLgFs = FontProperties(family='sans-serif', size=lgFs)

    # Assign ax and fig.
    if ax is None:
        ax = plt.gca()
    if fig is None:
        fig = plt.gcf()

    # Set figure size.
    fig.set_figwidth(figSize[0] / 2.54)
    fig.set_figheight(figSize[1] / 2.54)

    # Set axes and legend properties.
    if xLim is not None:
        ax.set_xlim(xLim)
    if yLim is not None:
        ax.set_ylim(yLim)

    if xTicks is not None:
        ax.set_xticks(xTicks)
    if yTicks is not None:
        ax.set_yticks(yTicks)

    if isinstance(xMajorTickFormat, int):
        strFormat = r'%.{}f'.format(xMajorTickFormat)
        xmajorFormatter = mTicker.FormatStrFormatter(strFormat)
        ax.xaxis.set_major_formatter(xmajorFormatter)
    elif xMajorTickFormat:
        ax.xaxis.set_major_formatter(xMajorTickFormat)

    if isinstance(yMajorTickFormat, int):
        strFormat = r'%.{}f'.format(yMajorTickFormat)
        ymajorFormatter = mTicker.FormatStrFormatter(strFormat)
        ax.yaxis.set_major_formatter(ymajorFormatter)
    elif yMajorTickFormat:
        ax.yaxis.set_major_formatter(yMajorTickFormat)

    if xMinorLocator == 'lin':
        ax.xaxis.set_minor_locator(mTicker.LinearLocator(
            numticks=2 * len(ax.xaxis.get_major_ticks()) - 1))
    elif xMinorLocator:
        ax.xaxis.set_minor_locator(xMinorLocator)

    if yMinorLocator == 'lin':
        ax.yaxis.set_minor_locator(mTicker.LinearLocator(
            numticks=2 * len(ax.yaxis.get_major_ticks()) - 1))
    elif yMinorLocator:
        ax.yaxis.set_minor_locator(yMinorLocator)

    [tickLabel.set_fontproperties(fontTickLs)
     for tickLabel in ax.get_xticklabels() + ax.get_yticklabels()]

    if xLabel is not None:
        ax.set_xlabel(xLabel, fontproperties=fontAxLs)
    if yLabel is not None:
        ax.set_ylabel(yLabel, fontproperties=fontAxLs)

    if legend is not None:
        if lgStyle.lower() == 'row':
            lg = plt.legend(legend, prop=fontLgFs, loc=3,
                            bbox_to_anchor=(0, 1.02, 1.0, 0), ncol=len(legend),
                            borderaxespad=0., mode='expand')
            frame = lg.get_frame()
            frame.set_linewidth(0.5)
        else:
            lg = plt.legend(legend, prop=fontLgFs, loc=6,
                            bbox_to_anchor=(1.02, 0.5), borderaxespad=0.)
            frame = lg.get_frame()
            frame.set_linewidth(0.5)

    if disp:
        plt.show()

    if save:
        fig.savefig(figName + '.' + fmt, format=fmt,
                    bbox_inches='tight', transparent=True)


# Usage example
if (__name__ == "__main__"):
    import numpy as np

    figDefault()

    x = np.linspace(1, 600) / 180 * np.pi
    y = np.sin(x)
    plt.plot(x, y)
    figPrint('Eg_sin', fmt='png', xLim=(0, 12), xMajorTickFormat=2,
             xMinorLocator='lin', disp=True, save=True)
