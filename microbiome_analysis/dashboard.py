import streamlit as st
from microbiome_analysis.visualization import plot_alpha_diversity, plot_beta_diversity, plot_pca

def create_dashboard(data, diversity_df, pca_coords, labels):
    st.title("Microbiome Analysis Dashboard")
    st.write("## Microbiome Composition")
    st.plotly_chart(plot_alpha_diversity(diversity_df))
    st.write("## Diversity Analysis")
    st.plotly_chart(plot_beta_diversity(pca_coords, method='PCoA'))
    st.write("## PCA Analysis")
    plot_pca(pca_coords, labels)
