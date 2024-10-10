from numpy.random import random

from utils.dataframes_util import random_dataframe, corrupt_dataframe, compare_dataframes

if __name__ == '__main__':
    # Variables
    COLUMNS = ["Foo", "Bar", "Baz"]
    DATASET_SIZE = 2500000  # Original dataset size
    CONFIDENCE = 0.999999  # Desired level of confidence that datasets are identical (here: 1/1000).
    NUMBER_OF_ERRORS = 100  # Max 'allowed' number of errors
    RANDOM_STATE = random(100500)
    CORRUPTION_FACTOR = 0.001
    SOURCE_TARGET = ("src", "trg")

    width = len(COLUMNS)
    print(f"Dataset size = {DATASET_SIZE} rows x {width} columns; {DATASET_SIZE * width} cells.")
    print(
        f"Corrupted cells in target dataframe, approximately ({CORRUPTION_FACTOR}%): {DATASET_SIZE * width * (CORRUPTION_FACTOR / 100)} cells.")
    # Let's generate our dataframes
    source_dataframe = random_dataframe(DATASET_SIZE, COLUMNS, 0, 2)
    target_dataframe = corrupt_dataframe(source_dataframe, CORRUPTION_FACTOR)

    # Evaluating sample size
    error_rate = NUMBER_OF_ERRORS / DATASET_SIZE
    diff = compare_dataframes(source_dataframe, target_dataframe, CONFIDENCE, error_rate)

    print(f"{diff}\nDifference in sample ({diff.shape[0]} rows, {diff.notna().sum().sum()/2} cells)")

    diff.to_csv("./results/diff_sampled.csv")

    print("Results are saved to ./results")
