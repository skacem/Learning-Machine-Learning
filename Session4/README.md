#  Session 4 - Introduction to Logistic Regression

## Motivation

Contrary to what its name suggests, logistic regression is a classification problem. In fact, when it comes to solving classification problems or to predict binomial outcomes (y = 0 or 1), logistic regression should be the first supervised learning type algorithm that we think of. In my opinion, everyone who is into machine learning should have acquired a strong foundation of Logistic Regression and the theory behinds it. Aside from being fundamental, powerful, and easy to implement, logistic regressions basic theoretical concepts are integral to understanding deep learning.

Furthermore, in the business world, classification problems where the response or dependent variable have discrete and finitet outcomes, are more prevalent than the regression problems where the response variable is continuous and have infinite values. That makes logistic regression one of the most common algorithm used for modeling classification problems.

In this serie of notebooks, we introduce logistic regression, and specifically show how logistic regression can be performed on a case study. We also introduce several popular performance metrics and show how they can be calculated for binary classification tasks. 


## Case Study: The Challenger Disaster

The Space Shuttle Challenger exploded 73 second after liftoff on January 28th, 1986. The disaster claimed the lives of all seven astronauts on board, including the first ordinary citizen ever allowed to fly to the space, a school teacher Christa McAuliffe. The details surrounding this disaster were very involved ( For more information see [video](https://bit.ly/3fPqAc1))

For the purposes of this analysis, it is sufficient to point out that engineers that manufactured the large boosters that launched the rocket were aware of the possible failures that could happen in the O-rings during cold temperatures. They tried to prevent the launch, but were ultimately ignored and disaster ensued.

The data consists of 5 attributes:
1. `Number`: Number of O-rings at risk on a given flight
2. `Number_TD`: Number experiencing thermal distress
3. `Temperature`: Launch temperature (degree F)
4. `Pressure`: Leak-check pressure (psi)
5. `Order`: Temporal order of flight

The feature that we want to predict is `Number_TD`, which corresponds to the number of thermal failures. It only takes one TD failure toget a fatal outcome. So we are interested in p = 0 which means successful mission and anything else is fatal, which is the probability for at least one o-ring failing for the given launch: TD > 0 or (1 - p).