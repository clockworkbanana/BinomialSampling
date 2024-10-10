import pandas as pd
import numpy as np
from numpy.random import randint

import utils.binomial_sampling as sample
from decorators.info import info


@info
def random_dataframe(size: int, columns: list[str], min_value=0, max_value=100) -> pd.DataFrame:
    return pd.DataFrame(np.random.randint(min_value, max_value, size=(size, len(columns))), columns=columns)

@info
def corrupt_dataframe(original: pd.DataFrame, percentage: float):
    corrupted_copy = original.copy(deep=True)
    number_of_cells = round(original.shape[0] * original.shape[1] * (percentage / 100))

    for i in range(number_of_cells):
        random_row = np.random.randint(0, original.shape[0])  # Random row index
        random_col = np.random.randint(0, original.shape[1])  # Random column index
        random_new_value = np.random.randint(0, 100)

        corrupted_copy.iat[random_row, random_col] = random_new_value  # Assign a new value

    return corrupted_copy


@info
def compare_dataframes(source: pd.DataFrame, target: pd.DataFrame,
                       confidence: float = 0.999, error_rate: float = 0.01) -> pd.DataFrame:
    sample_size = sample.sample_size_er(confidence, error_rate)
    random_state = randint(0, 10000)

    source_sample = source.sample(n=sample_size, random_state=random_state)
    target_sample = target.sample(n=sample_size, random_state=random_state)

    return source_sample.compare(target_sample, result_names=("src", "trg"))
