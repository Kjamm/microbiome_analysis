import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def create_cooccurrence_network(data):
    adjacency_matrix = (data.T @ data)
    adjacency_matrix.values[np.triu_indices_from(adjacency_matrix, 1)] = 0
    network = nx.from_pandas_adjacency(adjacency_matrix)
    return network

def plot_network(network):
    pos = nx.spring_layout(network)
    nx.draw(network, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()

def analyze_network_centrality(network):
    centrality = nx.degree_centrality(network)
    return centrality