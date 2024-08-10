import pandas as pd
import numpy as np
from scipy.stats import entropy

def shannon_index(counts):
    proportions = counts / np.sum(counts)
    return entropy(proportions)

def simpson_index(counts):
    proportions = counts / np.sum(counts)
    return 1 - np.sum(proportions**2)

def calculate_alpha_diversity(data):
    shannon = data.apply(shannon_index, axis=1)
    simpson = data.apply(simpson_index, axis=1)
    return pd.DataFrame({'shannon': shannon, 'simpson': simpson})