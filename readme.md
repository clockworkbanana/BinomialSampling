# Binomial sampling approach

## Problem

We have two datasets (tables).
One is expected to be an exact copy of another, say, result of data migration.
How much pairs of records do I need to check to reach desired level of confidence that datasets match?

## Variables

N - Dataset size\
C - Confidence\
b - expected number of errors ('bad' record)\
p = b/N - error rate (probability the record is corrupted)\
S - sample size

## Evaluations

We pick a random pair.The probability that it is correct is:
$$(1-P)$$
We pick S random pairs. The probability (confidence level C) that they all correct is:
$$
C = (1-p)^S ≈ e^{-pS} \\
$$

$$
=> S = F(C,P) = \frac{-ln(1-C)}{P}
$$

$$
<=>
$$

$$
S = F(C,N,b) = \frac{-ln(1-C)}{b/N}
$$
Please mind that this approach assumes that the dataset is pretty large.
Will go crazy for smaller datasets and higher levels of confidence.
