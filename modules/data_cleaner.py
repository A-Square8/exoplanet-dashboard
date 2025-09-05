import pandas as pd

def clean_data(df):
    key_columns = ['disc_year', 'discoverymethod', 'pl_rade', 'ra', 'dec', 'sy_dist', 'pl_orbper', 
                   'pl_insol', 'st_teff', 'st_lum', 'pl_orbsmax', 'sy_vmag']
    df = df.dropna(subset=key_columns)
    df = df[df['pl_orbper'] < 1e6]
    return df





    # Drop rows with NaN in key columns (expanded for complexity)
    # Handle outliers: Cap extreme values (e.g., orbital period > 1e6 days)