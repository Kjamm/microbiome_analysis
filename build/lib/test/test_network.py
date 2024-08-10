import unittest
import pandas as pd
from microbiome_analysis import network

class TestNetwork(unittest.TestCase):

    def test_create_cooccurrence_network(self):
        data = pd.DataFrame({
            'sample1': [10, 20, 30],
            'sample2': [20, 30, 40]
        })
        network_graph = network.create_cooccurrence_network(data)
        self.assertIsNotNone(network_graph)

    def test_plot_network(self):
        data = pd.DataFrame({
            'sample1': [10, 20, 30],
            'sample2': [20, 30, 40]
        })
        network_graph = network.create_cooccurrence_network(data)
        network.plot_network(network_graph)

    def test_analyze_network_centrality(self):
        data = pd.DataFrame({
            'sample1': [10, 20, 30],
            'sample2': [20, 30, 40]
        })
        network_graph = network.create_cooccurrence_network(data)
        centrality = network.analyze_network_centrality(network_graph)
        self.assertIsNotNone(centrality)

if __name__ == '__main__':
    unittest.main()
