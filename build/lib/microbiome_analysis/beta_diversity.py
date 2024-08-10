from sklearn.decomposition import PCA
from sklearn.metrics import pairwise_distances
from sklearn.manifold import MDS

def pca_analysis(data):
    pca = PCA(n_components=2)
    return pca.fit_transform(data)

def pcoa_analysis(data, metric='braycurtis'):
    dist_matrix = pairwise_distances(data, metric=metric)
    pca = PCA(n_components=2)
    return pca.fit_transform(dist_matrix)

def nmds_analysis(data, metric='braycurtis'):
    dist_matrix = pairwise_distances(data, metric=metric)
    nmds = MDS(n_components=2, dissimilarity='precomputed')
    return nmds.fit_transform(dist_matrix)
