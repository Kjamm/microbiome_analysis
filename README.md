# Microbiome Analysis
[ENGLISH](https://github.com/Kjamm/microbiome_analysis) [한국어](https://github.com/Kjamm/microbiome_analysis/blob/main/README_KOR.md)

![image](https://github.com/user-attachments/assets/16626a5d-413d-48ec-bf53-c55698a14619)

This library was created out of the personal curiosity of Jaemin Kim of Chungnam National University.

A comprehensive Python library for microbiome data analysis, providing functionalities for data processing, quality control, normalization, diversity analysis, visualization, network analysis, and statistical comparisons.

## Features

- **Data Input & Transformation**: Support for various file formats (CSV, Excel, FASTQ, FASTA) and integration of metadata with sequence data.
- **Quality Control**: Sequence quality assessment, filtering, and consistency checks across samples.
- **Normalization & Filtering**: Sample size normalization, rare sequence removal, and background noise filtering.
- **Diversity Analysis**: Calculation of various alpha and beta diversity indices.
- **Taxonomic Classification**: Sequence classification using pre-trained classifiers.
- **Visualization**: Plotting diversity indices, PCA/PCoA/NMDS results, and network visualizations.
- **Network Analysis**: Co-occurrence network creation and centrality analysis.
- **Statistical Analysis**: ANOVA, PERMANOVA, differential abundance analysis, and correlation analysis.
- **Interactive Dashboard**: Streamlit-based dashboard for data visualization and exploration.

## Installation

To install the library, use the following command:

```bash
pip install microbiome_analysis
```

## Usage
Below are examples of how to use various features of the library.

## Data Input & Transformation

```python
from microbiome_analysis import preprocessing

# Read sequences from a FASTQ file
sequences = preprocessing.read_fastq("example.fastq")

# Read metadata from a CSV file
metadata_df = preprocessing.read_csv("metadata.csv")

# Merge metadata with sequence data
merged_data = preprocessing.merge_metadata_sequence(metadata_df, sequences)
```

## Quality Control
```python
from microbiome_analysis import qc

# Perform quality control on sequences
qualities = qc.quality_control(sequences)

# Plot quality score distribution
qc.plot_quality_distribution(sequences)

# Check consistency across samples
samples = [sequences, sequences]  # Example list of sample sequences
consistency = qc.check_consistency(samples)
print(f"Consistency across samples: {consistency}")
```

## Normalization & Filtering
```python
from microbiome_analysis import normalization

# Normalize sample sizes
normalized_data = normalization.normalize_sample_size(data)

# Remove rare sequences
filtered_data = normalization.remove_rare_sequences(data, threshold=10)

# Filter background noise
cleaned_data = normalization.filter_background_noise(data, noise_threshold=0.01)
```

## Diversity Analysis
```python
from microbiome_analysis import diversity

# Calculate alpha diversity indices
alpha_diversity = diversity.calculate_alpha_diversity(data)
print(alpha_diversity)
```

## Beta Diversity Analysis
```python
from microbiome_analysis import beta_diversity

# Perform PCA analysis
pca_coords = beta_diversity.pca_analysis(data)

# Perform PCoA analysis
pcoa_coords = beta_diversity.pcoa_analysis(data)

# Perform NMDS analysis
nmds_coords = beta_diversity.nmds_analysis(data)
```

## Taxonomic Classification
```python
from microbiome_analysis import classification

# Train the classifier
sequences = [
    'ATCGGCTAAG',
    'GCTTAGCTAG',
    'TTCGCTGATC',
    'GCTAGCTAGT'
]
labels = [
    'species_1',
    'species_2',
    'species_1',
    'species_2'
]
trained_classifier = classification.train_classifier(sequences, labels)

# Classify new samples
new_samples = [
    'ATCGGCTAAG',
    'GCTAGCTAGT'
]
predicted_labels = classification.classify_new_samples(new_samples, trained_classifier)
print(predicted_labels)
```

## Visualization
```python
from microbiome_analysis import visualization

# Plot alpha diversity indices
visualization.plot_alpha_diversity(alpha_diversity)

# Plot PCA results
visualization.plot_pca(pca_coords, labels)

# Plot beta diversity results
visualization.plot_beta_diversity(pcoa_coords, method='PCoA')
```

## Network Analysis
```python
from microbiome_analysis import network

# Create co-occurrence network
cooccurrence_network = network.create_cooccurrence_network(data)

# Plot network
network.plot_network(cooccurrence_network)

# Analyze network centrality
centrality = network.analyze_network_centrality(cooccurrence_network)
print(centrality)
```

## Statistical Analysis
```python
from microbiome_analysis import statistics

# Perform ANOVA analysis
anova_result = statistics.anova_analysis(groups)
print(anova_result)

# Perform PERMANOVA analysis
permanova_result = statistics.perm_anova(data, groups)
print(permanova_result)

# Perform correlation analysis
correlation_result = statistics.correlation_analysis(data1, data2, method='spearman')
print(correlation_result)
```

## Interactive Dashboard
```python
from microbiome_analysis import dashboard

# Create an interactive dashboard
data = pd.DataFrame({
    'feature1': [10, 20, 30],
    'feature2': [20, 30, 40]
})
diversity_df = pd.DataFrame({
    'shannon': [1.0, 2.0, 3.0],
    'simpson': [0.5, 0.3, 0.2]
})
pca_coords = pd.DataFrame({
    'PC1': [1.0, 2.0, 3.0],
    'PC2': [0.5, 0.3, 0.2]
})
labels = ['label1', 'label2', 'label3']
dashboard.create_dashboard(data, diversity_df, pca_coords, labels)
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## License
This project is licensed under the MIT License.
