#%%
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def animate_contour(x_k, X, Y, Z, function_latex, f):
    fig, ax = plt.subplots(figsize = (7,7))
    ax.contour(X, Y, Z, 100, cmap = 'jet')
    ax.set_title(f"GradientDescent contour plot of {function_latex}")

    line, = ax.plot([], [], 'r', label = 'GD', lw = 1.5)
    point, = ax.plot([], [], '*', color = 'red', markersize = 4)
    value_display = ax.text(0.02, 0.02, '', transform=ax.transAxes)

    def init_1():
        line.set_data([], [])
        point.set_data([], [])
        value_display.set_text('')

        return line, point, value_display

    def animate_1(i):
        # Animate line
        line.set_data(x_k[:i,0], x_k[:i, 1])
        
        # Animate points
        point.set_data(x_k[i, 0], x_k[i, 1])
        
        # Values
        value_display.set_text(f'$f(\\theta) =${f(x_k[i][0][0], x_k[i][1][0]):.4f}')
        
        # Axis
        plt.ylabel("$Y$")
        plt.xlabel("$X$")

        return line, point, value_display

    ax.legend(loc = 1)

    anim = animation.FuncAnimation(fig, animate_1, init_func=init_1, frames=len(x_k), interval=20,
                                    repeat_delay=60, blit=True)
    if not os.path.exists('plots'):
        os.makedirs('plots')
    anim.save(os.path.join('plots', "GD_contour.gif"), writer='ffmpeg')

def animate_surface(x_k, X, Y, Z, function_latex, f):
         
    z_history = np.zeros(len(x_k))
     
    for i in range(len(x_k)):
        z_history[i] = x_k[i][0]**2 + x_k[i][1]**2
     
    z_history = z_history.reshape((len(x_k)))
     
    new_x_k = x_k.reshape((len(x_k) * 2))
     
    x_history = new_x_k[::2]
    y_history = new_x_k[1::2]
      
    fig = plt.figure(figsize = (7,7))
    ax = plt.axes(projection ='3d')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.set_zlabel('$Z$')
     
    ax.plot_surface(X, Y, Z, cmap = plt.cm.CMRmap, edgecolor ='green', alpha = 0.5)
    ax.set_title(f"GradientDescent surface plot of {function_latex}")
     
    ax.view_init(40, 75)
     
    line, = ax.plot([], [], [], 'r', label = 'GD', lw = 1.5)
    point, = ax.plot([], [], [], '*', color = 'red', markersize = 4)
    value_display = ax.text(0.02, 0.02, z =0.02, s= '', transform=ax.transAxes)
     
    def init_2():
        line.set_data_3d([], [], [])
        point.set_data_3d([], [], [])
        value_display.set_text('')
        return line, point, value_display
     
    def animate_2(i):
        line.set_data_3d(x_history[:i], y_history[:i], z_history[:i])
        # Animate points
        point.set_data_3d([x_history[i]], [y_history[i]], [z_history[i]])
        value_display.set_text(f'$f(\\theta) =${f(x_k[i][0][0], x_k[i][1][0]):.4f}')
        return line, point, value_display
     
    ax.legend(loc = 1)
     
    anim = animation.FuncAnimation(fig, animate_2, init_func=init_2, frames=len(x_k),
                                   interval=20,repeat_delay=60, blit=False)
    if not os.path.exists('plots'):
        os.makedirs('plots')
    anim.save(os.path.join('plots', "GD_surface.gif"), writer='ffmpeg')