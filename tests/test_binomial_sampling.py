import unittest
from utils.binomial_sampling import sample_size_er, sample_size_ne


class TestBinomialSampling(unittest.TestCase):

    def setUp(self):
        self.dataset_size = 250000000
        self.confidence = 0.99999
        self.number_of_errors = 250
        self.error_rate = 0.01

    def tearDown(self):
        pass

    def test_sample_size_ar(self):
        self.assertEqual(11512925, sample_size_ne(self.confidence, self.dataset_size, self.number_of_errors))

    def test_sample_size_er(self):
        self.assertEqual(1151, sample_size_er(self.confidence, self.error_rate))


if __name__ == '__main__':
    unittest.main()
