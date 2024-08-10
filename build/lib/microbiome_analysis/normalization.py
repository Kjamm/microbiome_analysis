import numpy as np

def normalize_sample_size(data):
    min_size = min(data.sum(axis=1))
    normalized_data = data.div(data.sum(axis=1), axis=0).multiply(min_size)
    return normalized_data

def remove_rare_sequences(data, threshold=10):
    return data.loc[:, (data > threshold).sum(axis=0) > 0]

def filter_background_noise(data, noise_threshold=0.01):
    return data.loc[:, (data / data.sum()).sum(axis=0) > noise_threshold]
