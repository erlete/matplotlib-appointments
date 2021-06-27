"""Simple 'matplotlib.pyplot' module components testing script."""

import matplotlib.pyplot as plt
import numpy as np


def basic_plot():
    """The most basic representation."""
    y_axis = [1, 2, 3, 4, 5]

    plt.plot(y_axis)
    plt.show()


def np_basic_plot():
    """Slightly more advanced representation, featuring 'numpy' module."""
    x_axis = np.arange(1, 101)
    y_axis = x_axis ** 2

    plt.plot(x_axis, y_axis)
    plt.show()


def labels():
    """X and Y axis label setting."""
    x_axis = np.arange(1, 101)
    y_axis = x_axis ** 2

    plt.suptitle('Superior title')
    plt.title('Normal title')
    plt.xlabel('X axis title')
    plt.ylabel('Y axis title')
    plt.plot(x_axis, y_axis)

    plt.show()


def sub_plot():
    """Distribution of a figure in several subplots."""
    fig = plt.figure()
    plt.suptitle('Four graphs plot')

    x_axis = np.arange(1, 101)
    y_axis_1 = x_axis ** 2
    y_axis_2 = x_axis ** (1 / 2)
    y_axis_3 = 1 / x_axis
    y_axis_4 = np.log(x_axis)

    plt.subplot(2, 2, 1)
    plt.title('Squared')
    plt.plot(x_axis, y_axis_1)

    plt.subplot(2, 2, 2)
    plt.title('Square root')
    plt.plot(x_axis, y_axis_2)

    plt.subplot(2, 2, 3)
    plt.title('Inverse')
    plt.plot(x_axis, y_axis_3)

    plt.subplot(2, 2, 4)
    plt.title('Logarithmic')
    plt.plot(x_axis, y_axis_4)

    plt.show()
    plt.close(fig)


def design():
    """Design factors that modify the appearance of the figures and plots."""
    fig = plt.figure()
    plt.suptitle('Customised graphs')

    x_axis = np.arange(1, 101)
    y_axis_1 = x_axis ** 2
    y_axis_2 = x_axis ** (1 / 2)
    y_axis_3 = 1 / x_axis
    y_axis_4 = np.log(x_axis)

    plt.subplot(2, 2, 1)
    plt.title('Solid line')
    plot_1 = plt.plot(x_axis, y_axis_1)
    plt.setp(
        plot_1,
        color='red',
        linestyle='solid',
        linewidth=.25,
    )

    plt.subplot(2, 2, 2)
    plt.title('Dashed line with markers and 80x, 20y limits')
    plot_2 = plt.plot(x_axis, y_axis_2)
    plt.setp(
        plot_2,
        color='blue',
        linestyle='dashed',
        linewidth=.50,
        marker='+',
        markeredgecolor='orange',
        markeredgewidth=1.5,
        markerfacecolor='red',
        markersize=7.5,
        markevery=10
    )
    plt.xlim(0, 80)
    plt.ylim(0, 20)

    plt.subplot(2, 2, 3)
    plt.title('Dimmed dashdot line with markers and grid')
    plot_3 = plt.plot(x_axis, y_axis_3)
    plt.setp(
        plot_3,
        alpha=.25,
        color='violet',
        linestyle='dashdot',
        linewidth=2.5,
        marker='.',
        markeredgecolor='orange',
        markeredgewidth=1.5,
        markerfacecolor='red',
        markersize=7.5,
        markevery=10
    )
    plt.grid(True)

    plt.subplot(2, 2, 4)
    plt.title('Dotted line with markers and grid')
    plot_4 = plt.plot(x_axis, y_axis_4)
    plt.setp(
        plot_4,
        color='blue',
        linestyle='dotted',
        linewidth=5.0,
        marker='1',
        markeredgecolor='orange',
        markeredgewidth=1.5,
        markerfacecolor='red',
        markersize=10.0,
        markevery=10
    )
    plt.grid(True)

    plt.show()
    plt.close(fig)


def annotations():
    """Ways to insert annotations in the plots."""
    fig = plt.figure()
    x_axis = np.arange(0.0, 5.0, 0.01)
    y_axis = np.cos(2 * np.pi * x_axis)
    plt.plot(x_axis, y_axis)
    plt.annotate(
        'Local Maximum',
        xy=(2, 1),
        xytext=(2, 2),
        arrowprops=dict(
            facecolor='black',
            arrowstyle='-|>'
        ),
    )
    plt.grid(True)
    plt.ylim(-4, 4)

    plt.show()
    plt.close(fig)


def settings_list():
    """A simple list of possible settngs for the 'plt.setp' method."""
    print("""
    - agg_filter: a filter function, which takes a (m, n, 3) float array and a
        dpi value, and returns a (m, n, 3) array
    - alpha: float or None
    - animated: bool
    - antialiased or aa: bool
    - clip_box: `.Bbox`
    - clip_on: bool
    - clip_path: Patch or (Path, Transform) or None
    - color or c: color
    - contains: unknown
    - dash_capstyle: {'butt', 'round', 'projecting'}
    - dash_joinstyle: {'miter', 'round', 'bevel'}
    - dashes: sequence of floats (on/off ink in points) or (None, None)
    - data: (2, N) array or two 1D arrays
    - drawstyle or ds: {'default', 'steps', 'steps-pre', 'steps-mid',
        'steps-post'} default: 'default'
    - figure: `.Figure`
    - fillstyle: {'full', 'left', 'right', 'bottom', 'top', 'none'}
    - gid: str
    - in_layout: bool
    - label: object
    - linestyle or ls: {'-', '--', '-.', ':', '', 'solid', 'dash', 'dashdot',
        'dotted', (offset, on-off-seq), ...}
    - linewidth or lw: float
    - marker: {'+', ',', '.', '1', '2', '3', '4'}
    - markeredgecolor or mec: color
    - markeredgewidth or mew: float
    - markerfacecolor or mfc: color
    - markerfacecoloralt or mfcalt: color
    - markersize or ms: float
    - markevery: None or int or (int, int) or slice or List[int] or float or
        (float, float) or List[bool]
    - path_effects: `.AbstractPathEffect`
    - picker: unknown
    - pickradius: float
    - rasterized: bool or None
    - sketch_params: (scale: float, length: float, randomness: float)
    - snap: bool or None
    - solid_capstyle: {'butt', 'round', 'projecting'}
    - solid_joinstyle: {'miter', 'round', 'bevel'}
    - transform: `matplotlib.transforms.Transform`
    - url: str
    - visible: bool
    - xdata: 1D array
    - ydata: 1D array
    - zorder: float
    """)


basic_plot()
np_basic_plot()
labels()
sub_plot()
design()
annotations()
settings_list()
