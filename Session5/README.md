# Introduction to Decision Trees

## Motivation
In this session, we introduce the Decision Tree algorithm, and demonstrate how to effectively use this algorithm for both classification and regression problems. The Decision Tree algorithm is another simple algorithm that can be easy to understand, since a higher level representation of the data is iteratively constructed from the data. Different approaches to building decision trees have been developed, they differ primarily in the ways the higher level representation is constructed. In the end, a decision tree provides a powerful, predictive model that can capture non-linear effects while also being easy to understand and explain.

## Introduction

One of the simplest machine learning algorithms to understand is the decision tree. For a classification task, a decision tree asks a set of questions of the data, and based on the answers determines the final classification. 

In addition to their simplicity, decision trees have a number of other benefits. First, they are a _white box model_, which simply means we can understand exactly why a decision tree makes a specific prediction on a given instance. Second, they can handle both numerical and categorical data, and they do not require pre-processing beyond handling missing values. Trees also tend to perform well on large data sets.

On the other hand, decision trees are prone to overfitting; where they model the training data too well and do not generalize to unseen data. Decision trees can have difficulty classifying on unbalanced classes and they can be unstable to minor changes in the training data. Overall, however, the decision tree is one of a handful of standard machine learning algorithms with which you should be familiar.


A decision tree uses if-then statements to define patterns in data.

In machine learning, these statements are called forks, and they split the data into two branches based on some value.

That value between the branches is called a split point. Homes to the left of that point get categorized in one way, while those to the right are categorized in another. A split point is the decision tree's version of a boundary.