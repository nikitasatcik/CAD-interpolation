import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

"""
Spline interpolation of CAD data. CAD data cross-section is stored as X,Y poit-pairs in .csv file.
2023-04-28 by Mykyta Kolchiba.
"""

def get_xy_curve_from_csv(path):
    with open(path, "r") as file:
        vals = [val.strip().split(',') for val in file.readlines()]
        x_ = [float(val[0]) for val in vals]
        y_ = [float(val[1]) for val in vals]

    # x values must be in strictly increasing order.
    if not np.all(np.diff(x_) > 0):
        x_, y_ = x_[::-1], y_[::-1]

    return np.array(x_), np.array(y_)


def plot_xy_curve(x, y, cs, npts):
    x_fit = np.linspace(x.min(), x.max(), npts)
    y_fit = cs(x_fit)
    
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(x_fit, y_fit, 'o', label='fitted data')
    ax.plot(x, cs(x), label='spline')
    ax.legend(loc='lower right', ncol=2)
    
    print('x        y')
    print('----------')
    for xi, yi in zip(x_fit, y_fit):
        print(f'{xi:.3f}  {yi:.3f}')
    plt.show()
    

x, y = get_xy_curve_from_csv("C:\\Users\\user\\Documents\\Python Scripts\\tir_1.csv")
cs = CubicSpline(x, y)
plot_xy_curve(x, y, cs, 25)


        
    
