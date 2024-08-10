from setuptools import setup, find_packages

setup(
    name="microbiome_analysis",
    version="0.1.0",
    description="A Python library for microbiome data analysis",
    author="Your Name",
    author_email="your.email@example.com",
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
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)