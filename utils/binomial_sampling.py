import math

from decorators.info import info

# Thoughts
"""
N - Dataset size
C - Confidence
p - error rate (probability the error is corrupt)
b - expected number of errors ('bad' record)
S - sample size
The size of the sample can be evaluated based on ERROR_RATE or NUMBER_OF_ERRORS.
                    P = b/N
Evaluation:
We pick a random pair. The probability that it is correct is:
                    (1 - р)
We pick S random pairs. The probability (confidence level C) that they all correct is:
             C = (1-p)^S ≈ e^-pS
       => S = F(C,P) = -ln(1-C) / P
                    OR
        S = F(C,N,b) = -ln(1-C) / (b/N)

Please mind that this approach assumes that the dataset is pretty large.
Will go crazy for smaller datasets.
e.g. 10 records dataset would require 100+ sample size to achive high level of confidence
"""


# Functions
@info
def sample_size_er(confidence: float, error_rate: float) -> int:
    """
    Estimates the size of sample to be taken from a dataset to achieve
    desired level of confidence within specified error rate

    :param confidence: percents. Can be decimal
    :param error_rate: 'allowed' error rate. E.g.: 0.01 - 1 of 100 records
    :return:
    """
    return round(-math.log(1 - confidence) / error_rate)


@info
def sample_size_ne(confidence: float, dataset_size: int, number_errors: int) -> int:
    """
    Estimates the size of sample to be taken from a dataset to achieve
    desired level of confidence within specified number of errors.

    :param confidence: confidence (decimal)
    :param dataset_size: the initial size of the dataset
    :param number_errors: 'allowed number of errors'
    :return: Suggested sample size = f ()
    """
    error_rate = number_errors / dataset_size
    return sample_size_er(confidence, error_rate)
