import unittest
import pandas as pd
from microbiome_analysis import visualization

class TestVisualization(unittest.TestCase):

    def test_plot_alpha_diversity(self):
        diversity_df = pd.DataFrame({
            'shannon': [1.0, 2.0, 3.0],
            'simpson': [0.5, 0.3, 0.2]
        })
        visualization.plot_alpha_diversity(diversity_df)

    def test_plot_pca(self):
        coords = pd.DataFrame({
            'PC1': [1.0, 2.0, 3.0],
            'PC2': [0.5, 0.3, 0.2]
        })
        labels = [1, 2, 3]
        visualization.plot_pca(coords, labels)

    def test_plot_beta_diversity(self):
        coords = pd.DataFrame({
            'Dim1': [1.0, 2.0, 3.0],
            'Dim2': [0.5, 0.3, 0.2]
        })
        visualization.plot_beta_diversity(coords, method='PCoA')

if __name__ == '__main__':
    unittest.main()
