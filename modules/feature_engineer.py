import pandas as pd
import numpy as np

def engineer_features(df):
    def get_planet_type(rade):
        if rade < 1.5: return 'Rocky'
        elif 1.5 <= rade < 4: return 'Super-Earth'
        elif 4 <= rade < 10: return 'Neptune-like'
        else: return 'Gas Giant'
    df['planet_type'] = df['pl_rade'].apply(get_planet_type)
    
    
    df['st_lum_solar'] = 10 ** df['st_lum']  
    df['hz_inner'] = np.sqrt(df['st_lum_solar'] / 1.1)
    df['hz_outer'] = np.sqrt(df['st_lum_solar'] / 0.53)
    def get_hz_class(orbsmax, inner, outer):
        if orbsmax < inner: return 'Inner Habitable'
        elif inner <= orbsmax <= outer: return 'Habitable'
        elif orbsmax > outer: return 'Outer Habitable'
        else: return 'Not Habitable'
    df['hz_class'] = df.apply(lambda row: get_hz_class(row['pl_orbsmax'], row['hz_inner'], row['hz_outer']), axis=1)
    
    return df




# Complex: Custom habitable zone classification using stellar params
# Formula: Inner HZ (AU) ≈ sqrt(L_star / 1.1), Outer HZ ≈ sqrt(L_star / 0.53) where L_star = 10^st_lum (Solar)
# Classify based on pl_orbsmax