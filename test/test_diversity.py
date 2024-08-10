import unittest
import pandas as pd
from microbiome_analysis import diversity

class TestDiversity(unittest.TestCase):

    def test_calculate_alpha_diversity(self):
        data = pd.DataFrame({
            'sample1': [10, 20, 30],
            'sample2': [20, 30, 40]
        })
        alpha_diversity = diversity.calculate_alpha_diversity(data)
        self.assertIsNotNone(alpha_diversity)

if __name__ == '__main__':
    unittest.main()
