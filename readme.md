# Binomial sampling approach

## Problem

We have two datasets (tables).
One is expected to be an exact copy of another, say, as a result of data migration.
How much pairs of records do I need to check to reach desired level of confidence that datasets match?

## Variables

N - Dataset size\
C - Confidence\
b - maximum theoretical number of 'escaped' (corrupted records)\
p = b/N - error rate (probability the record is corrupted)\
S - sample size - **that's the value we want to calculate**

## Evaluations

We pick a random pair.The probability that it is correct is:

$$(1-p)$$

We pick S random pairs. The probability (confidence level C) that they all correct is:

$$C = (1-p)^S ≈ e^{-pS}$$

$$=> S = F(C,p) = \frac{-ln(1-C)}{p}$$

$$<=>$$

$$S = F(C,N,b) = \frac{-ln(1-C)}{b/N}$$

Please mind that this approach assumes that the dataset is pretty large.
Will go crazy for smaller datasets and higher levels of confidence.
