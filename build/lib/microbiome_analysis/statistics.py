from scipy.stats import f_oneway, spearmanr, pearsonr
import statsmodels.api as sm
import pandas as pd

def anova_analysis(groups):
    return f_oneway(*groups)

def perm_anova(data, groups):
    return sm.stats.anova_lm(data, typ=2)

def lefse_analysis(data, groups):
    # Placeholder for LEfSe analysis
    pass

def deseq2_analysis(data, groups):
    # Placeholder for DESeq2 analysis
    pass

def correlation_analysis(data1, data2, method='spearman'):
    if method == 'spearman':
        return spearmanr(data1, data2)
    elif method == 'pearson':
        return pearsonr(data1, data2)
    else:
        raise ValueError("Method must be 'spearman' or 'pearson'")