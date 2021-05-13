# Learning ML and AI
(Work in progress. Inspired by Robert J. Brunner from the University of Illinois)

## Repo Description

Welcome to learning machine learning. This is a comprehensive guide for an inspiring manager or MBA student to learn about machine learning use cases and business application. It is a work in progress and reflects my personal journey in learning about ML.

## Objectives
The following are the primary learning objectives:
1. Articulate the importance of machine learning in management decision making
2. Acquire skills and techniques that can be applied immediately to today's digital economy
3. Write effective machine learning workflows by using Python
4. Know your key performance indicators

## Prerequisites
None

## Session 0 - Motivation
Let's start with some interesting readings:
1.  [Machine learning, explained](https://bit.ly/2PYjQ2M) by Sara Brown, MIT Management SLOAN School 2021
2.  [What Every Manager Should Know About Machine Learning](https://bit.ly/3e8cDGx) by Mike Yeomans, HBR 2015
3.  [An executive’s guide to machine learning](https://mck.co/3ujlaMI) By Dorian Pyle and Cristina San José, Mckinsey 2015
4.  [How is the accountancy and finance world using artificial intelligence?](https://bit.ly/3nWvtnb) by Eleanor O'Neil, 2019
5.  [Strategic leadership for the digital economy](https://bit.ly/3tuDHnQ) by Meredith Somers, MIT Sloan 2021

## Session 1 - An Interactive Overview about ML Algorithm Using Scikit-Learn

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/skacem/Learning-Machine-Learning/main?filepath=MLOverview.ipynb)       [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/skacem/Learning-Machine-Learning/blob/main/MLOverview.ipynb) [![Heroku](https://ml-interactive-overview.herokuapp.com/?app=ml-interactive-overview)]

Broadly speaking, the application of a machine learning algorithm will be one of four different categories:

* **Classification**: generates a model that predicts discrete categories for new, unseen data.
* **Regression**: generates a model that predicts continuous values for new, unseen data.
* **Dimensionality reduction**: identifies (and optionally ranks) the most important (potentially new) features (or dimensions) for a data set.
* **Clustering**: identifies clusters of instances in an  𝑁 -dimensional feature space.

The general approach to using `scikit-learn` is to follow the following steps:

1. Given the application type (classification, regression, dimensional reduction, or clustering) create the appropriate `scikit-learn` estimator.
2. Determine the best Hyperparameters
3. Extract the feature matrix, and if appropriate, the target vector (our labels array)
4. Apply the `fit` method for the selected estimator to generate a best fit model.
5. Apply the generated model to new data by calling the:
    * predict method for classification and regression applications,
    * transform method for dimensional reduction applications, and 
    * either predict or transform for clustering applications, depending on whether data are being assigned to clusters (predict) or the data are being converted so that the distances from each data point to each cluster center are computed (transform)
6. Finally, as appropriate, the efficacy of the machine learning algorithm can be computed for test data by calling an appropriate score method (and other available performance metrics)

Scikit-learn library estimators are sensitive to variations in the spread of features within a data set. The algorithm might focus on the one feature with a larger spread, even if this produces a sub-optimal result. To prevent this, we generally scale the features to improve the performance of a given scikit-learn estimastor.

Data scaling in scikit-learn can take several forms:
* **Standardization**: the data are scaled to have zero mean and unit (i.e. one) variance.
* **Normalization**: the data are scaled to have unit mean and variance.
* **Range**: the data are scaled to span a defined range, such as [0, 1]
* **Binarization**: the data are thresholded such that values below the threshold are zero (or False), and above the threshold are one (or True)

*Any scaling technique should be trained via the `fit` method on the training data. Once trained, the scaling technique can be applied equally to the training and testing data.*

