import unittest
import pandas as pd
from microbiome_analysis import statistics

class TestStatistics(unittest.TestCase):

    def test_anova_analysis(self):
        groups = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        result = statistics.anova_analysis(groups)
        self.assertIsNotNone(result)

    def test_perm_anova(self):
        data = pd.DataFrame({
            'group1': [1, 2, 3],
            'group2': [4, 5, 6],
            'group3': [7, 8, 9]
        })
        result = statistics.perm_anova(data, groups=['group1', 'group2', 'group3'])
        self.assertIsNotNone(result)

    def test_correlation_analysis(self):
        data1 = [1, 2, 3]
        data2 = [4, 5, 6]
        result = statistics.correlation_analysis(data1, data2, method='spearman')
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
