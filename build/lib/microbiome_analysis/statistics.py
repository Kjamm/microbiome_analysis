from scipy.stats import f_oneway, spearmanr, pearsonr
import statsmodels.api as sm
import pandas as pd


def anova_analysis(groups):
    return f_oneway(*groups)


def perm_anova(data, groups):
    """
    Perform PERMANOVA analysis on the provided data.

    Parameters:
    data (pd.DataFrame): The data to analyze.
    groups (list): A list of group names.

    Returns:
    result: ANOVA table.
    """
    formula = 'value ~ C(group)'
    data_melted = pd.melt(data.reset_index(), id_vars=['index'], value_vars=groups)
    data_melted.columns = ['index', 'group', 'value']
    model = sm.OLS.from_formula(formula, data=data_melted).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    return anova_table


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
