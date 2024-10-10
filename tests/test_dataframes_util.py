import unittest

from utils.dataframes_util import random_dataframe, corrupt_dataframe, compare_dataframes


class TestDataframesUtil(unittest.TestCase):

    def setUp(self):
        self.dataset_size = 250000000
        self.confidence = 0.999
        self.number_of_errors = 250
        self.error_rate = 0.001

    def tearDown(self):
        pass

    def test_random_dataframe(self):
        df = random_dataframe(100, ["Alpha", "Bravo", "Charlie", "Delta", "Echo"])
        height = df.shape[0]
        width = df.shape[1]

        self.assertEqual(height, 100)
        self.assertEqual(width, 5)

    def test_corrupt_dataframe(self):
        columns = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
        rows = 10
        corruption_factor = 5

        max_corrupted_rows = round(len(columns) * rows * (corruption_factor / 100))

        df = random_dataframe(rows, columns)
        df_corrupted = corrupt_dataframe(df, corruption_factor)

        diff = df.compare(df_corrupted)

        diff_size = diff.shape[0]

        self.assertGreater(diff_size, 0)
        self.assertLessEqual(diff_size, max_corrupted_rows)

    def test_compare_dataframes_positive(self):
        columns = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
        rows = 1000
        df = random_dataframe(rows, columns)

        diff = compare_dataframes(df, df)

        self.assertEqual(diff.shape[0], 0)

    def test_compare_dataframes_negative(self):
        """
        This test may fail one run out of 100 due to randomized nature of data sampling.
        Statistically it should work with confidence of 0.999 and error rate of 0.01
        """
        columns = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
        rows = 100000
        corruption_factor = 0.1  # One of 1000 records is corrupted

        max_corrupted_rows = round(len(columns) * rows * (corruption_factor / 100))

        df = random_dataframe(rows, columns)
        df_corrupted = corrupt_dataframe(df, corruption_factor)

        diff = compare_dataframes(df, df_corrupted)

        diff_size = diff.shape[0]

        self.assertGreater(diff_size, 0)
        self.assertLessEqual(diff_size, max_corrupted_rows)


if __name__ == '__main__':
    unittest.main()
