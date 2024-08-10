import pandas as pd
from Bio import SeqIO

def read_csv(file_path):
    return pd.read_csv(file_path)

def read_excel(file_path):
    return pd.read_excel(file_path)

def read_fastq(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fastq"):
        sequences.append(record)
    return sequences

def read_fasta(file_path):
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(record)
    return sequences

def merge_metadata_sequence(metadata_df, sequences):
    metadata_df['sequence'] = [str(seq.seq) for seq in sequences]
    return metadata_df
