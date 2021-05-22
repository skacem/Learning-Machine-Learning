# k-Nearest Neighbor (k-nn)

## Introduction

k-nn is one of the simplest machine learning algorithms, that is used to perform both classification and regression. It is different than most other algorithms in several ways:
* First the algorithm is a lazy learner in that no model is constructed. The predictions are made straight from the training data. Thus, the fit method doesn't build a model, it instead builds an efficient representation of the training data.
* Second, this algorithm is non-linear and non-parametric since no model is constructed

It is based on the principle that data values in an $N$- dimensional space are generally located near other similar objects. The number of nearest neighbors, `k`, is a tuning parameter, and can be specified a priori, or in some algorithms empirically determined.

## Distance Measurements
Fundamental to this algorithm is the concept of metric. Formally, a metric defines how distances are measured for a particular set of data.  
The scikit-learn library supports different distance metrics in the neighbors module. Some of the standard metrics in this module include:

* `euclidean`: supports the standard concept of spatial distance, and is the l2-norm
* `manhattan`: restricts distance measurements to follow grid lines. This metric is sometimes referred to as the Taxi cab distance, since taxis must follow streets, which also gives rise to its formal name, _manhattan_, for the street grid on the island of Manhattan. This distance is also known as the `l1-norm`.
* `haversine`
* `chebyshev`
* `minkowski`

## Curse of Dimensionality

In general, we strive to obtain as much as data as possible to improve our model prediction. The additional data can take one of two forms: 

1. Additional features, which increases the dimensionality of our data set
2. Additional instances, which increases the pool of data from which to draw training and testing samples... And more data requires more computational power.

Additional dimensions on the other hand, can introduce an additional complication that is known as the *curse of dimensionality*.

At its simplest, the curse of dimensionality relates the density of training data to the performance of our machine learning algorithm. In order to ensure sufficient density of training data across a potential sample space, the quantity of training data must increase exponentially (or very rapidly) with each new dimension. Otherwise, we end up with a space that is poorly sampled by training data.

To overcome the curse of dimensionality, one must either increase the amount of training data, or reduce the dimensionality by either identifying the most important features or deriving new features that contain most of the information. This is what we call **feature engineering**.

## Notebook - Iris Data

In this Notebook, we will use the standard Iris classification data set to explore how to perform basic classification tasks.