import pandas as pd
from pandasql import sqldf
from scipy import stats
import numpy as np

def compute_metrics(filtered_df):
    discovery_counts = filtered_df.groupby('disc_year').size().reset_index(name='counts')
    
   
    env = {'filtered_df': filtered_df}  
    pysqldf = lambda q: sqldf(q, env)
    method_counts_query = "SELECT discoverymethod, COUNT(*) as count FROM filtered_df GROUP BY discoverymethod"
    method_counts = pysqldf(method_counts_query)
  
    num_cols = ['pl_rade', 'pl_orbper', 'pl_insol', 'st_teff', 'st_lum', 'pl_orbsmax', 'sy_vmag']
    corr_matrix = filtered_df[num_cols].corr()
    
    # Complex: ANOVA test - Do planet radii differ by discovery method?
    methods = filtered_df['discoverymethod'].unique()
    groups = [filtered_df[filtered_df['discoverymethod'] == m]['pl_rade'] for m in methods if len(filtered_df[filtered_df['discoverymethod'] == m]) > 1]
    if len(groups) > 1:
        anova_f, anova_p = stats.f_oneway(*groups)
        anova_result = f"ANOVA F-stat: {anova_f:.2f}, p-value: {anova_p:.4f} (Significant difference if p < 0.05)"
    else:
        anova_result = "Insufficient groups for ANOVA"
    

    avg_brightness = filtered_df['sy_vmag'].mean()
    
    return {
        'discovery_counts': discovery_counts,
        'method_counts': method_counts,
        'corr_matrix': corr_matrix,
        'anova_result': anova_result,
        'avg_brightness': avg_brightness
    }

def get_habitable_planets(filtered_df):
    habitable = filtered_df[filtered_df['hz_class'] == 'Habitable']
    return habitable