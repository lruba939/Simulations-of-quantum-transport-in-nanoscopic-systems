import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import get_cmap
import numpy as np

# Global settings for plotting

## Font
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 14

## Lines
rcParams['lines.solid_joinstyle'] = 'miter'  # other options: 'round' or 'bevel'
rcParams['lines.antialiased'] = True  # turning on/off of antialiasing for sharper edges
rcParams['lines.linewidth'] = 1

## Legend
rcParams['legend.loc'] = 'upper left'
rcParams['legend.frameon'] = False

## Ticks
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'
rcParams['xtick.top'] = True
rcParams['ytick.right'] = True

rcParams['xtick.minor.visible'] = True
rcParams['ytick.minor.visible'] = True

## Resolution
rcParams['figure.dpi'] = 150

## Colors
### cmaps
cm_inferno = get_cmap("inferno")
cm_viridis = get_cmap("viridis")
cm_seismic = get_cmap("seismic")
cm_jet = get_cmap("jet")
cm_tab10 = get_cmap("tab10")
### Palettes from color-hex.com/
c_google = ['#008744', '#0057e7', '#d62d20', '#ffa700'] # G, B, R, Y # https://www.color-hex.com/color-palette/1872
c_twilight = ['#363b74', '#673888', '#ef4f91', '#c79dd7', '#4d1b7b'] # https://www.color-hex.com/color-palette/809


# Get array of colors from cmap
def cm2c(cmap, c_numb, step=6):
    if c_numb > step:
        step = c_numb
    
    colors_arr = []
    for i in range(c_numb):
        colors_arr.append(cmap(i / step))
    
    return colors_arr

def map_plotter(data, ax=None, cm=cm_inferno, xlabel="x [nm]", ylabel="y [nm]", 
                xborder=None, yborder=None, ticks_step=2, vmin=None, vmax=None, 
                equal_aspect=True, title=None, show_colorbar=True):

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 3.2))
    
    if equal_aspect:
        ax.set_aspect('equal')

    extent = None
    if xborder is not None and yborder is not None:
        ax.set_xlim(-xborder, xborder)
        ax.set_ylim(-yborder, yborder)

        while (xborder % ticks_step != 0 and yborder % ticks_step != 0):
            ticks_step += 1
            if ticks_step > 5:
                ticks_step = 1
                break

        ax.set_xticks(np.linspace(-xborder, xborder, round(ticks_step * 2) + 1))
        ax.set_yticks(np.linspace(-yborder, yborder, round(ticks_step * 2) + 1))

        extent = [-xborder, xborder, -yborder, yborder]
    elif xborder is not None or yborder is not None:
        print("\n\nPlotting error!\nBoth 'xborder' and 'yborder' must be provided.\n")

    im = ax.imshow(data, interpolation='none', origin='lower', extent=extent, cmap=cm, vmin=vmin, vmax=vmax)
    ax.tick_params(direction="out", which="both")

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if title is not None:
        ax.set_title(title)

    if show_colorbar:
        plt.colorbar(im, ax=ax, orientation='vertical')

    return ax

def map_grid_plotter(data_list, n, m, **kwargs):
    fig, axes = plt.subplots(n, m, figsize=(4*m, 4*n))
    
    axes = np.atleast_2d(axes).reshape(-1)

    for i, data in enumerate(data_list):
        if i >= len(axes):
            break
        map_plotter(data, ax=axes[i], show_colorbar=False, **kwargs)

    for j in range(len(data_list), len(axes)): # empty subplots if no data
        axes[j].axis("off")

    plt.tight_layout()
    plt.show()