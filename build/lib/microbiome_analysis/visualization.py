import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

def plot_alpha_diversity(diversity_df):
    fig = px.box(diversity_df)
    fig.show()

def plot_pca(coords, labels):
    coords = np.array(coords)
    fig = plt.figure()
    plt.scatter(coords[:, 0], coords[:, 1], c=labels)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('PCA')
    plt.show()
    return fig

def plot_beta_diversity(coords, method='PCoA'):
    fig = px.scatter(coords, x='Dim1', y='Dim2', title=method)
    fig.show()
