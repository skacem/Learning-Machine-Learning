from matplotlib import cm
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




def make_lr_plot(ind_train, dep_train, ind_test, dep_test, results, labels=['Control Variable', 'Response']):
    """
    Plotting function to show both regression fit to the data and the residual plot
    """

    # Set up plot area
    sns.set(style="white")
    fig, axs = plt.subplots(figsize=(10, 8), nrows=2, ncols=1, 
                            sharex=True)

    # Add space between plots
    fig.subplots_adjust(hspace=0.5)

    # Plot the training and testing data
    axs[0].scatter(ind_train, dep_train, label='Training Data',
               alpha = .5, cmap=cm.coolwarm)
    axs[0].scatter(ind_test, dep_test, label='Testing Data',
               alpha = .5, cmap=cm.coolwarm)

    # Plot model prediction
    axs[0].plot(ind_test, results, label='Model', c='r', alpha = .25)
    
    # Ensure equal axis
    axs[0].set_aspect('equal')

    # Decorate final plot
    axs[0].set_xlabel(labels[0], fontsize=14)
    axs[0].set_ylabel(labels[1], fontsize=14)
    axs[0].set_title("Regression Plot", fontsize=18)
    axs[0].set_xlim(-2, 52)
    axs[0].set_ylim(-1, 10)
    axs[0].legend()    
    sns.despine(ax=axs[0], trim=True)
    
    # Plot model residuals
    axs[1].scatter(ind_test, dep_test - results, label='Testing Data',
               alpha = .5, cmap=cm.coolwarm)

    # Show zero residual line
    axs[1].hlines(0, 0, 50, color='r', linestyle='--', alpha=0.25)

    # Decorate final plot
    axs[1].set_xlabel(labels[0], fontsize=14)
    axs[1].set_ylabel("Residual", fontsize=14)
    axs[1].set_title("Regression Plot (model residuals)", fontsize=18)
    axs[1].set_ylim(-5, 5)
    sns.despine(ax=axs[1], trim=True)