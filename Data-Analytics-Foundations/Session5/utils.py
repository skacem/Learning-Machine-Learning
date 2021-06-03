import numpy as np
import pandas as pd
import seaborn as sns
# Create Colormaps for the plots
from matplotlib.colors import ListedColormap

# 2 Dimension iris data
def trim_data(d_train_sc, l_train):
    """
    Trim the Full Iris data set to two dimensions
    (Sepal Width and Petal Width)
    return the data with attached labels
    """
    
    data = np.zeros((d_train_sc.shape[0], 3))
    data[:, 0] = d_train_sc[:, 1]
    data[:, 1] = d_train_sc[:, 3]
    data[:, 2] = l_train[:]
    
    return data

# Convenience function to plot confusion matrix
def confusion(test, predict, title):
    """
    This method produces a colored heatmap that displays the relationship
    between predicted and actual types from a machine learning method.
    """
    
    # Define names for the three Iris types
    names = ['Setosa', 'Versicolor', 'Virginica']

    # Make a 2D histogram from the test and result arrays
    # pts is essentially the output of the scikit-learn
    # confusion_matrix mathod
    pts, xe, ye = np.histogram2d(test, predict, bins=3)

    # For simplicity we create a new DataFrame for the confusion matrix
    pd_pts = pd.DataFrame(pts.astype(int), index=names, columns=names )
    
    # Display heatmap and add decorations
    hm = sns.heatmap(pd_pts, annot=True, fmt="d")
    hm.axes.set_title(title, fontsize=20)
    hm.axes.set_xlabel('True Label', fontsize=18)
    hm.axes.set_ylabel('Predicted Label', fontsize=18)

    return None

def get_mdata(data, grid_size = 100):
    """
    Make a uniformly spaced grid of points across the space occupied by our data.
    We assume a datsets is passed into this function that has two dimensions
    coresponding to x, y
    """
    
    # We grab the min and max of the points, and make the pace a bit bigger.
    # We could make this dynamic.
    
    x_min, x_max = data[:, 0].min() - .25, data[:, 0].max() + .25
    y_min, y_max = data[:, 1].min() - .25, data[:, 1].max() + .25

    # Meshgrid gives two 2D arrays of the ppoints
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, grid_size),
                         np.linspace(y_min, y_max, grid_size))
    
    # We want to return these points as an array of two-dimensional points
    return np.c_[xx.ravel(), yy.ravel()]


# Plot data for comparison
def splot_data(ax, data, mdata, z, label1, label2, sz, grid_size = 100):
    """
    Plot the data and mesh for comparison
    """

    cmap_back = ListedColormap(sns.hls_palette(3, l=.4, s=.1))
    cmap_pts = ListedColormap(sns.hls_palette(3, l=.9, s=.9))

    ax.set_aspect('equal')

    # Decorate the plot
    ax.set_xlabel(label1)
    ax.set_ylabel(label2)
    
    # We need grid points and values to make the colormesh plot
    xx = mdata[:, 0].reshape((grid_size, grid_size))
    yy = mdata[:, 1].reshape((grid_size, grid_size))
    zz = z.reshape((grid_size, grid_size))

    ax.pcolormesh(xx, yy, zz, cmap=cmap_back, alpha = 0.9)
    
    # Now draw the points, with bolder colors.
    ax.scatter(data[:, 0], data[:, 1], c=data[:, 2], s=sz, cmap=cmap_pts)
    
    
# Modified example at scikit learn:
# http://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html
def random_cosine(xhigh, num_pts, randomstate):
    """
    Create random data consisting of a _cosine_ with additional random perturbations
    xhigh: Maximum range in x
    num_pts: Number of points for model
    """
    # Make the data
    rns = np.random.RandomState(randomstate)

    # Generate random data and convert to an ordered list by sorting
    x = np.sort(xhigh * rns.rand(num_pts, 1), axis=0)

    # Generate dependent variable as the cosine plus noise.
    y = np.cos(x) + (0.5 - rns.rand(num_pts, 1))

    # Generate uniform sampling points.
    xx = np.linspace(0, xhigh, num_pts * 5)[:, np.newaxis]
    
    return x, y, xx