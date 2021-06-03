# Time Series Modeling

In this session we are going to analyze three different practical cases of time series:
1. Google trends of the word "vacation"
2. Stock
3. Global warming

We are going to introduce the two main time series models, namely:
additive model and multiplicative model. 

The focus, however, is going to be on seasonality, trends and noise and how to get rid of them using `statsmodels` library.

We are also going to learn how to use `pytrends` to perform google trends queries. how to plot auto-correlation and partial auto-correlation functions and the differences between both.

## Components of a Time Series

A time series is composed of mainly trend, seasonality and noise. We will take a look at the component parts of a time series, focusing on automated decomposition methods.

## Trend
When we talk about trend, we are talking about how the series data increases or decreases over time. Is it moving higher or lower over the time frame? The series is either uptrend or downtrend, both of which are non-stationary.

## Seasonality
Seasonality refers to a repeating periodic or cyclical pattern with regular intervals within a series. The pattern is within a fixed time period and it repeats itself at regular intervals. There can be upward or downward swings but it continues to repeat over a fixed period of time as in a cycle. Cyclicality could repeat but it has no fixed period.

## Noise
In general, noise captures the irregularities or random variation in the series. It can have erratic events or simply random variation. It has a short duration. It is hard to predict due to its erratic orrcurence