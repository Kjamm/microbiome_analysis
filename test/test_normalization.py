import unittest
import pandas as pd
from microbiome_analysis import normalization

class TestNormalization(unittest.TestCase):

    def test_normalize_sample_size(self):
        data = pd.DataFrame({
            'sample1': [10, 20, 30],
            'sample2': [20, 30, 40]
        })
        normalized_data = normalization.normalize_sample_size(data)
        self.assertIsNotNone(normalized_data)

    def test_remove_rare_sequences(self):
        data = pd.DataFrame({
            'sequence1': [1, 2, 3],
            'sequence2': [10, 20, 30]
        })
        filtered_data = normalization.remove_rare_sequences(data, threshold=5)
        self.assertIsNotNone(filtered_data)

    def test_filter_background_noise(self):
        data = pd.DataFrame({
            'sequence1': [1, 2, 3],
            'sequence2': [10, 20, 30]
        })
        cleaned_data = normalization.filter_background_noise(data, noise_threshold=0.01)
        self.assertIsNotNone(cleaned_data)

if __name__ == '__main__':
    unittest.main()
