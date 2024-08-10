import matplotlib.pyplot as plt
import seaborn as sns

def quality_control(sequences):
    quality_scores = []
    for seq in sequences:
        quality_scores.extend(seq.letter_annotations["phred_quality"])
    return quality_scores

def plot_quality_distribution(sequences):
    qualities = quality_control(sequences)
    sns.histplot(qualities, bins=50)
    plt.xlabel('Quality Score')
    plt.ylabel('Frequency')
    plt.title('Quality Score Distribution')
    plt.show()

def check_consistency(sample_list):
    lengths = [len(sample) for sample in sample_list]
    return all(x == lengths[0] for x in lengths)
