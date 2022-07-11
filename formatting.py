from matplotlib import cm
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.colors as matcolors
import matplotlib.pyplot as plt


def std_plot(fs: tuple[int, int]=(8,8)) -> tuple[Figure, Axes]:
    return plt.subplots(figsize=fs)


def set_tex_font() -> None:
    """Enables LaTeX font for plot labels."""
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "sans-serif",
        "font.sans-serif": ["Computer Modern Serif"]}
        )
    return


def no_tex() -> None:
    """Disables LaTeX font for plot labels."""
    plt.rcParams.update({
        "text.usetex": False,
        "font.family": "serif",
        "font.serif": ["DejaVu Sans"]}
        )
    return


def format_ax(ax: Axes, xlog: bool=False, ylog: bool=False, **kwargs) -> Axes:
    
    ax.tick_params(labelsize=24, which='both')
    
    if xlog:
        ax.set_xscale('log')
    if ylog:
        ax.set_yscale('log')

    fontsize = kwargs['fontsize'] if 'fontsize' in kwargs else 20

    if 'xlab' in kwargs:
        ax.set_xlabel(kwargs['xlab'], fontsize=fontsize)
    if 'ylab' in kwargs:
        ax.set_ylabel(kwargs['ylab'], fontsize=fontsize)

    return ax


def color_gradient() -> list[tuple]:
    """Returns a list of seven color tuples."""
    norm = matcolors.Normalize(vmin=0, vmax=600)
    vir_col = [cm.viridis(norm(i*100),bytes=False) for i in range(7)]
    cool_col = [cm.Spectral(norm(i*100),bytes=False) for i in range(7)]
    cfb = (100/255,149/255,237/255,1.0) # 'cornflowerblue', Hex: #6495ED
    colors = [cool_col[0], cool_col[1], cool_col[2], vir_col[6], vir_col[5], vir_col[3],  cfb]
    return colors

    
def viridis_gradient(n_colors: int = 7) -> list[tuple]:
    """Returns a list of colors from the viridis color scale."""
    norm = matcolors.Normalize(vmin=0, vmax=(n_colors-1)*100)
    viridis_col = [cm.viridis(norm(i*100),bytes=False) for i in range(n_colors)]
    return viridis_col
    