from setuptools import setup, find_packages

setup(
    name="microbiome_analysis",
    version="0.1.0",
    description="A comprehensive Python library for microbiome data analysis",
    author="Jaemin Kim",
    author_email="jaemin52577441@gmail.com",
    packages=find_packages(),
    install_requires=[
        "biopython",
        "numpy",
        "scipy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "plotly",
        "streamlit",
        "networkx",
        "statsmodels",
        "kaleido"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
