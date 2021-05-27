#  Session 4 - Introduction to Logistic Regression

## Motivation

Contrary to what its name suggests, logistic regression is a classification problem. In fact, when it comes to solving classification problems, logistic regression should be the first supervised learning type algorithm that we think of. In my opinion, everyone who is into machine learning should have acquired a strong foundation of Logistic Regression and the theory behinds it. Aside from being fundamental, powerful, and easy to implement, logistic regressions basic theoretical concepts are integral to understanding deep learning.

In this notebook, we introduce logistic regression, and specifically show how logistic regression can be performed by using estimators from the scikit-learn library. We also introduce several popular performance metrics and show how they can be calculated for binary classification tasks. 

## Theory
 In a binary classification process, we have two possible outcome, which we can label as Success or Failure. Denoting the probability of these outcomes as $P(S)$ and $P(F)$ respectively, we can write: 
 * the probability of susccess as $P(S) = p$,
 * probability of failure as $P(F) = 1 - p$ and
 * the odds of a successful outcome as $Odds(S) = \frac{p}{1-p}$.
 We can extend the framework of *linear regression* to the task of binary classification by employing a mapping between the continuous value predicted by a linear regressor and the probability of an event occurring, which is bounded by the range [0, 1]. Two functions do that:  `logit` function and `probit` function
 
 ## Logit Function
 the `logit function` is defined as the logarithm of the odds (i.e $p/(1-p)$), which is also known as the *log-odds*. Thus, the *logit* function can be written for a probability of success *p*:
 $$logit(p) = log(p/(p-1))$$, where $$0\leq p \leq 1$$
 
 We can invert this relationship to obtain the *logistic function*, which for a parameter $\alpha$ is defined by the following expression:

$\textrm{logit}^{-1}(\alpha) = \textrm{logistic}(\alpha) = \frac{1}{1 + \exp{(-\alpha})}$

While the logistic function is most commonly used to perform this type of regression, a related function is the _probit_ function, which stands for _probability unit_ and is sometimes used in lieu of the _logit_ function. The _probit_ function is defined for a probability of success, $p$:

$\textrm{probit}(p) = \sqrt{2}\erf^{-1}(2p - 1)$ where $0 \leq p \leq 1$, and $\erf$ is the Error Function.

The logit function (and the probit function) is an _S_ shaped curve that converts real numbers into a probability. Both the logit and probit functions are related to the _sigmoid_ function, but are centered at the origin (0, 0).