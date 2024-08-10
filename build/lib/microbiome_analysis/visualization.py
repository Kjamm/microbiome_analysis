import plotly.express as px
import matplotlib.pyplot as plt

def plot_alpha_diversity(diversity_df):
    fig = px.box(diversity_df)
    fig.show()

def plot_pca(coords, labels):
    fig = plt.figure()
    plt.scatter(coords[:, 0], coords[:, 1], c=labels)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('PCA')
    plt.show()
    return fig

def plot_beta_diversity(coords, method='PCoA'):
    fig = px.scatter(coords, x=0, y=1, title=method)
    fig.show()
