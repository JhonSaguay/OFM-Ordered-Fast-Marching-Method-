import numpy as np
import matplotlib.pyplot as plt
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

def contourgraph(matrixtime):
    
    n = len(matrixtime[0])
    m = len(matrixtime)
    x = np.arange(n)
    y = np.arange(m)
    X, Y = np.meshgrid(x, y)
    contours = plt.contour(X, Y, matrixtime,  colors='black',linestyles='dashed', linewidths=1)
    plt.clabel(contours, inline=True, fontsize=8)
    plt.imshow(matrixtime, extent=[0, n, 0, m], origin='lower',
           cmap='RdGy', alpha=0.5)
    plt.colorbar()
    plt.show()
    
def contour3dgraph(matrixtime):
    n = len(matrixtime[0])
    m = len(matrixtime)
    fig=p.figure()
    x = np.arange(n)
    y = np.arange(m)
    X, Y = np.meshgrid(x, y)
    Z=matrixtime
    ax = p3.Axes3D(fig)
    # ax.contourf3D(X,Y,Z)
    # ax.plot_wireframe(X,Y,Z)
    # ax.plot3D(np.ravel(X),np.ravel(Y),np.ravel(Z))
    ax.plot_surface(X, Y, Z, cmap=plt.cm.jet)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # fig.add_axes(ax)
    p.show()